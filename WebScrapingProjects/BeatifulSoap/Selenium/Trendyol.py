from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd


# test işlemleri için url'ler
url = 'https://www.trendyol.com/'
#url = 'https://www.trendyol.com/sr?q=ayakkab%C4%B1&qt=ayakkab%C4%B1&st=ayakkab%C4%B1&os=1'
#url = 'https://www.trendyol.com/sr?wb=44&wc=114&qt=ayakkab%C4%B1&st=ayakkab%C4%B1&vr=size|22&os=1'
#url = 'https://www.trendyol.com/sr?wb=44&wc=114&vr=size|22&prc=2000-2250&qt=ayakkab%C4%B1&st=ayakkab%C4%B1&os=1'

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_experimental_option('detach', True)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.get(url)

wait = WebDriverWait(driver, 10)
action = ActionChains(driver)

def cookie_and_advert(the_driver):
    close_advert = the_driver.find_element(By.CSS_SELECTOR,'div.modal-close')
    action.click(close_advert).perform()
    sleep(1)
    cookies = the_driver.find_element(By.CSS_SELECTOR,'button#onetrust-accept-btn-handler')
    action.click(cookies).perform()

def searching(the_driver):
    input_send = the_driver.find_element(By.CSS_SELECTOR,'input.vQI670rJ')
    input_send.send_keys('ayakkabı')
    sleep(1)

    input_search = the_driver.find_element(By.CSS_SELECTOR,'i.ft51BU2r')
    action.click(input_search).perform()
    sleep(1)

def filtering(the_driver):
    wait = WebDriverWait(driver, 10)
    checkbox = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.chckbox')))
    action.click(checkbox).perform()
    sleep(2)

    filtre_div = driver.find_element(By.CSS_SELECTOR, 'div.aggrgtn-cntnr-wrppr')  # örnek filtre div'i
    driver.execute_script("arguments[0].scrollTop += 50;", filtre_div)
    sleep(1)

    size_div = the_driver.find_element(By.CSS_SELECTOR, 'div.fltr-item-text')
    size_num =size_div.find_element(By.XPATH ,'//div[text()="22"]')
    driver.execute_script("arguments[0].scrollIntoView(true);", size_num)
    action.click(size_num).perform()
    sleep(2)

cookie_and_advert(driver)
searching(driver)
filtering(driver)

sleep(1)
#filtreledikten sonra kaç ürün olduğunu ekrana yazdırır.
product_count = driver.find_element(By.CSS_SELECTOR,'div.dscrptn-V2').text
product_count = product_count.split()[5]
print(product_count)
start_time = time.time()

#aynı linkleri vermesin sözlükte tekrar olmaz.
loaded_products = set()
while True:
    elements = driver.find_elements(By.CSS_SELECTOR, "div.p-card-wrppr")
    loaded_products.update(elements)
    driver.execute_script("window.scrollBy(0, 800);")
    sleep(1)
    if len(loaded_products) >= int(product_count):  # başta alınan ürün sayısı ile karşılaştıdık.
        break

#testing işlemi için doğru scroll yapabilmiş miyim diye
products = driver.find_elements(By.CSS_SELECTOR, "div.p-card-wrppr")
print(f"Scroll edildikten sonra toplam ürün sayısı: {len(products)}")

#ürünlerin linkini buraya attım burda sonrasında listeleyip gerekli işlemleri yaptım.
products_links=[]
for product in products:
    try:
        a = product.find_element(By.CSS_SELECTOR, 'a.p-card-chldrn-cntnr')
        url = a.get_attribute('href')
        products_links.append(url)
    except Exception as e:
        print(f"hata: {e}")



excel_datas = []
# gerekli ekrana yazdırma ve excele kaydetmek için gerekli döngü
for i,product_link in enumerate(products_links):
    driver.get(product_link)
    product_name = driver.find_element(By.CSS_SELECTOR, 'h1.pr-new-br').text

    #bazı ürünlerde indirim uygulanıyor o yüzden class yapısı değişiyor o yüzden try exccept kullandım.
    try:
        try:
            product_price = driver.find_element(By.CSS_SELECTOR, 'span.prc-dsc').text.split()[0]
        except:
            product_price = driver.find_element(By.CSS_SELECTOR, 'p.discounted-price').text.split()[0]
    except Exception as e:
        print(f"Fiyat alınamadı: {e}")
        product_price = "Yok"


    # bazı ürünlerin başka satıcısı yok o yüzden hata almamak içn try kullandım.
    try:
        other_product_buttons = driver.find_elements(By.CSS_SELECTOR, 'a.show-all')
        # productların başka satıcısı varsa işlemleri yap
        if other_product_buttons:
            other_product_button = other_product_buttons[0]
            sleep(1)
            action.click(other_product_button).perform()
            sleep(1)
            other_product_div = driver.find_elements(By.CSS_SELECTOR, 'div.pr-mc-w')
            sleep(1)
            # başka satıcıların bilgileri divi varsa
            if other_product_div:
                sleep(0.5)
                print(f"-------------{i+1}.{product_name}--{product_price} TL------{product_link}----")
                for other_product in other_product_div:
                    other_seller_name = other_product.find_element(By.CSS_SELECTOR, 'a.seller-name-text').text
                    other_seller_link = other_product.find_element(By.CSS_SELECTOR, 'a.seller-name-text').get_attribute('href')
                    other_seller_price = other_product.find_element(By.CSS_SELECTOR, 'span.prc-dsc').text.split()[0]

                    print(f"Mağaza Adı:{other_seller_name} - Fiyatı:{other_seller_price} - Linki:{other_seller_link}\n")
                    #başka satıcısı olan producların bilgilerini ekle excele
                    try:
                        excel_datas.append({
                            "Name": product_name,
                            "Price": product_price,
                            "Link": product_link,
                            "Other Seller Name": other_seller_name,
                            "Other Seller Price": other_seller_price,
                            "Other Seller Link": other_seller_link
                        })
                    except Exception as e:
                        print(f"veriler kaydedilemedi hata: {e}")

            # bu kısımda da başka satıcı yoksa ekle ayrı bi else ekledim çünkü for un içine sadece
            # başka satıcısı olanların bilgilileri kaydediyor.
            else:
                print(f"{i+1}.{product_name} ve {product_price} TL ,{product_link}->için başka satıcı yok\n")
                try:
                    excel_datas.append({
                        "Name": product_name,
                        "Price": product_price,
                        "Link": product_link,
                        "Other Seller Name": "Yok",
                        "Other Seller Price": "Yok",
                        "Other Seller Link": "Yok"
                    })
                except Exception as e:
                    print(f"veriler kaydedilemedi hata: {e}")
        else:
            print(f"{i+1}.{product_name} ve {product_price}TL ,{product_link} ->için başka satıcı yok\n")
            try:
                excel_datas.append({
                    "Name": product_name,
                    "Price": product_price,
                    "Link": product_link,
                    "Other Seller Name": "Yok",
                    "Other Seller Price": "Yok",
                    "Other Seller Link": "Yok"
                })
            except Exception as e:
                print(f"veriler kaydedilemedi hata: {e}")

    except Exception as e:
        print(f"otherlerla ilgili hata var : {e}")



print(f'{len(products_links)} tane link var.')

#fazla veri olduğu için kaç saniye de çalıştığını merak ettim.
end_time_2 = time.time()
total_time_2 = end_time_2 - start_time  #570 saniye sürdü
print(f"En toplamda çalışma süresi: {total_time_2:.2f} saniye")

df = pd.DataFrame(excel_datas)
df.to_excel("trendyol.xlsx", index=False)
print("\n Veriler Excel dosyasına kaydedildi: trendyol_verileri.xlsx")
