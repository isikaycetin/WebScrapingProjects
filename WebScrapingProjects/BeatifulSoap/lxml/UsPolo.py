import requests
from lxml import html
from time import sleep
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
}

base_url = "https://tr.uspoloassn.com/c/t-shirt-all/?attributes_filterable_color=Sar%C4%B1"
page = 1

def scraping_products(products):

    for i,product in enumerate(products):
        product_link = product.xpath('.//a[@class="js-product-images-wrapper"]/@href')
        if product_link:
            product_url = "https://tr.uspoloassn.com" + product_link[0]
            response = requests.get(product_url, headers=headers)

            if response.status_code != 200:
                print(f"Sayfa  erişim hatası: {response.status_code}")
                break

            tree = html.fromstring(response.content)

            name = tree.xpath('//div[@class="product__name--detail"]/div/h1/text()')
            try:
                price = tree.xpath('//div[@class="product__payment--price"]/del/text()')
            except:
                price = tree.xpath('//div[@class="product__payment--price"]/ins/text()')

            print(f"{i+1}.{name[0]} => {price[0].split()[0]} =>{product_url}")

            try:
                excel_datas.append({
                    "name": name[0],
                   "price": price[0].split()[0],
                   "product_url": product_url
                 })
            except:
                print("kaydetme hatası")

excel_datas = []
while True:
    url = f"{base_url}&page={page}"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Sayfa {page} erişim hatası: {response.status_code}")
        break

    tree = html.fromstring(response.content)

    products = tree.xpath('//div[contains(@class, "product__listing--item") and contains(@class, "offer")]')

    if not products:
        print(f"Sayfa {page} - ürün bulunamadı. Döngü sonlandı.")
        break


    print(f"Sayfa {page} - {len(products)} ürün bulundu.")
    scraping_products(products)

    page += 1
    sleep(1)

df = pd.DataFrame(excel_datas)
df.to_excel("UsPolo.xlsx", index=False)
print("\n Veriler Excel dosyasına kaydedildi: UsPolo_verileri.xlsx")
