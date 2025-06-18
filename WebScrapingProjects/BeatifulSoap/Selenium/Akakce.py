from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd


url = 'https://www.akakce.com/cep-telefonu.html/134091,80000-90000tl'

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_experimental_option('detach', True)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.get(url)

wait = WebDriverWait(driver, 10)
action = ActionChains(driver)


count = driver.find_element(By.CSS_SELECTOR,'span.cti_v8').text.split()[0]
print(count)
wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'li.w')))

# sayfadali productların linklerini listeye ekleyen fonksiyon
def product_links(the_driver):
    product_links = []
    products = the_driver.find_elements(By.CSS_SELECTOR, 'li.w')
    for i,product in enumerate(products):
        link = product.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
        name = product.find_element(By.CSS_SELECTOR, 'a.pw_v8').get_attribute('title')
        # print(f"{i+1}.=>{name} => {link}")
        product_links.append(link)
    return product_links

# sayfaların içine girip datalarını scraping eden fonksiyon
excel_datas =[]
def scraping_page(the_driver, url):
    the_driver.get(url)
    try:
        WebDriverWait(the_driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.pdt_v8')))
        product_name = the_driver.find_element(By.CSS_SELECTOR, 'div.pdt_v8 h1').text

        try:
            product_price = the_driver.find_element(By.CSS_SELECTOR, 'span.pt_v8').text
        except:
            product_price = "Fiyat bulunamadı"

        sleep(1)
        # diğer satıcıların listeleri
        other_sellers = the_driver.find_elements(By.CSS_SELECTOR, 'ul#PL li')
        if other_sellers:
            print(f"\n- - - - - - - - {product_name}=>{url}- - - - - - - - - ")
            for seller in other_sellers:
                try:
                    try:
                        other_price_raw = seller.find_element(By.CSS_SELECTOR, 'span.pt_v8').text.strip()
                        other_price = other_price_raw.split()[0] if other_price_raw else "Fiyat Yok"
                    except:
                        other_price = "Fiyat Yok"

                    try:
                        other_link = seller.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
                    except:
                        other_link = "Link Yok"

                    # print(f"{other_price} => {other_link}")
                    excel_datas.append({
                        'Name':product_name,
                        'Price': product_price,
                        'Link': url,
                        'Other Price': other_price,
                        'Other Link': other_link
                    })
                except:
                    print(f"\n{product_name}=>{url} eksik bilgi var")
                    excel_datas.append({
                        'Name':product_name,
                        'Price': product_price,
                        'Link': url,
                        'Other Price': "YOK",
                        'Other Link': "Yok"
                    })
                    continue
        else:
            print(f"{product_name} için başka satıcı yok")

    except Exception as e:
        print(f"seletörlerde hata verdi : {e}")

#tüm dış sayfaları gezer sonraki butonuna click eder
while True:
    urls = product_links(driver)

    for url in urls:
        scraping_page(driver,url)

    try:
        # Sonraki butonuna click işlemi
        next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.p[title="Sonraki"]')))

        # Scroll yaptım çünkü clickleme de hata aldım çözümü bunda buldum
        driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top + window.pageYOffset - 100);", next_button)
        sleep(1)

        next_button.click()
        sleep(3)  # yeni sayfanın yüklenmesi için beklemek

    except Exception as e:
        print("Sonraki sayfa yok veya tıklama hatası:", e)
        break

df = pd.DataFrame(excel_datas)
df.to_excel("akakce.xlsx", index=False)
print("\n Veriler Excel dosyasına kaydedildi: akakce.xlsx")

# diğer yollar
# next_button = driver.find_element(By.CSS_SELECTOR, 'a.p')
# if next_button.is_enabled():  #form elemanlaı için kullanılır.
#     next_button.click()
# else:
#     print("Buton aktif değil, döngü sonlanıyor.")
#     break

# disabled_attr = next_button.get_attribute('disabled')
# if disabled_attr:
#     break