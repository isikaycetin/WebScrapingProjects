import time
import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd

url ='https://www.amazon.com.tr/s?k=laptop&__mk_tr_TR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss'

excel_datas= []

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

def scraping(the_soup):
    laptops = the_soup.find_all('div', class_='puis-card-container')
    for i, laptop in enumerate(laptops):
        laptop_link = laptop.find('a', class_='a-link-normal')

        if laptop_link:
            laptop_url = 'https://www.amazon.com.tr' + laptop_link.get('href')
            response = requests.get(laptop_url, headers=headers)
            detail_soup = BeautifulSoup(response.text, 'html.parser')

            # Marka
            tr_mark = detail_soup.find('tr', class_='po-brand')
            if tr_mark:
                td_tags = tr_mark.find_all('td')
                td_mark = td_tags[1].text.strip() if len(td_tags) > 1 else "Marka eksik"
            else:
                td_mark = "Marka yok"

            # Renk
            tr_color = detail_soup.find('tr', class_='po-color')
            if tr_color:
                td_tags = tr_color.find_all('td')
                td_color = td_tags[1].text.strip() if len(td_tags) > 1 else "Renk eksik"
            else:
                td_color = "Renk yok"

            # RAM
            tr_ram = detail_soup.find('tr', class_='po-ram_memory.installed_size')
            if tr_ram:
                td_tags = tr_ram.find_all('td')
                td_ram = td_tags[1].text.strip() if len(td_tags) > 1 else "RAM eksik"
            else:
                td_ram = "RAM bilgisi yok"

            print(f"{i+1}. {td_mark}  -  {td_color} -  {td_ram}")

            excel_datas.append({
                "Marka": td_mark,
                "Renk": td_color,
                "RAM": td_ram,
                "Link": laptop_url
            })
        else:
            print(f"{i+1}. Ürün linki bulunamadı")

page_number = 1
while True:
    print(f'\n{page_number}. Sayfa')
    url = f'https://www.amazon.com.tr/s?k=laptop&page={page_number}'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    scraping(soup)

    next_button = soup.find('a', class_='s-pagination-next')
    if next_button is None:
        print("Sayfa Kalmadı!!")
        break

    page_number += 1

df = pd.DataFrame(excel_datas)
df.to_excel("amazon_laptop_verileri.xlsx", index=False)
print("\n Veriler Excel dosyasına kaydedildi: amazon_laptop_verileri.xlsx")