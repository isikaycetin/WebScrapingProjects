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


url = 'https://www.yurtlarburada.com/'

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_experimental_option('detach', True)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.get(url)

wait = WebDriverWait(driver, 10)
action = ActionChains(driver)

#yurt arama
def searching(the_driver):
    actions = ActionChains(driver)
    input = the_driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
    actions.click(input).perform()
    sleep(1)

    listed = the_driver.find_element(By.CSS_SELECTOR, 'div.SelectMenu_select_menu_content__list__wenVr')
    item = listed.find_element(By.TAG_NAME, 'div')
    actions.click(item).perform()
    sleep(1)

    gender = the_driver.find_element(By.XPATH,'//p[text()="Yurt Tipi Seçiniz"]')
    actions.click(gender).perform()
    sleep(1)

    gender_listed = the_driver.find_element(By.XPATH,'//div[text()="Erkek Öğrenci Yurdu"]')
    actions.click(gender_listed).perform()
    sleep(1)

    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[text()="YURT ARA"]'))
    )
    actions.click(search).perform()

try:
  searching(driver)
except Exception as e:
    print(f'Aranılamadı, hata: {e}')

wait = WebDriverWait(driver, 10)
more_button = driver.find_element(By.XPATH,'//button[text()="Daha Fazla Gör"]')
action.click(more_button).perform()
sleep(1)

cards = driver.find_elements(By.CSS_SELECTOR,'div.dorm-tab__col')
print(f'{len(cards)} tane erkek yurdu var.')

wanted_town = {'Şişli', 'Fatih', 'Kağıthane', 'Beşiktaş'}
filtered_links = []
excel_datas=[]

cards = driver.find_elements(By.CSS_SELECTOR, 'div.dorm-tab__col')
for card in cards:
    try:
        town_element = card.find_element(By.CSS_SELECTOR, 'div.DormCard_dorm-card__title__DFQm9').find_element(By.TAG_NAME, 'small')
        town_text = town_element.text.strip()

        if ',' in town_text:
            filtered_town = town_text.split(',')[1].strip()
            if filtered_town in wanted_town:
                link_element = card.find_element(By.TAG_NAME, 'a')
                url = link_element.get_attribute('href')
                filtered_links.append((url, filtered_town))
    except Exception as e:
        print(f"Kartta hata: {e}")


for i, (url, ilce) in enumerate(filtered_links):
        driver.get(url)
        sleep(2)

        try:
         yurt_name = driver.find_element(By.CSS_SELECTOR,'div.dorm-header__title').text
         bed_count = driver.find_element(By.CSS_SELECTOR,'div.dorm-header-inf__txt').text
         adress = driver.find_element(By.CSS_SELECTOR,'div.dorm-top-address__title').text
         tel_no = driver.find_element(By.CSS_SELECTOR,'a.dorm-top-address__title').text
         try:
             food_elements = driver.find_elements(By.CSS_SELECTOR, 'div.dorm-header-inf__txt')
             if len(food_elements) > 1:
                 food_count = food_elements[1].text
             else:
                 food_count = "Yemek bilgisi yok"
         except Exception:
             food_count = "hata Yemek bilgisi yok"

        except Exception as e:
            print(f"hata: {e}")

        print(f'{ilce} ilçesindeki yurda yönlendiriliyor {url}')
        print(f"----------{i+1}.yurt-------------")
        print(f"İsim: {yurt_name}")
        print(f"Yatak Sayısı: {bed_count}")
        print(f"Yemek Bilgisi: {food_count}")
        print(f"Adres: {adress}")
        print(f"Telefon: {tel_no}")
        print("-" * 30)

        try:
         excel_datas.append({
             "İsim": yurt_name,
             "Yatak Sayısı": bed_count,
             "Yemek Bilgisi": food_count,
             "Adres": adress,
             "Telefon":tel_no
         })
        except Exception as e:
            print(f"veriler kaydedilemedi hata: {e}")

df = pd.DataFrame(excel_datas)
df.to_excel("yurtlar_burda_verileri.xlsx", index=False)
print("\n Veriler Excel dosyasına kaydedildi: yurtlar_burda_verileri.xlsx")