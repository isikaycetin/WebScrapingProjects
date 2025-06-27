from time import sleep
import requests
import time
import pandas as pd

cookies = {

}

headers = {
}

params = {
    'wc': '104156',
    'wb': '794',
    'lc': '104156',
    'qt': 'televizyon',
    'st': 'televizyon',
    'os': '1',
    'pi': '1',
    'culture': 'tr-TR',
    'userGenderId': '1',
    'pId': '0',
    'isLegalRequirementConfirmed': 'false',
    'searchStrategyType': 'DEFAULT',
    'productStampType': 'TypeA',
    'scoringAlgorithmId': '2',
    'fixSlotProductAdsIncluded': 'true',
    'location': 'null',
    'channelId': '1',
}



params['pi'] = 1
total_products = 0
excel_datas = []
while True:
    base_url='https://apigw.trendyol.com/discovery-web-searchgw-service/v2/api/infinite-scroll/sr'
    response = requests.get(url=base_url,params=params,cookies=cookies,headers=headers,timeout=15)

    if response.status_code != 200:
        print(f"Hata oluştu. Kod: {response.status_code}")
        break

    data = response.json()
    result = data.get('result')

    if not result or not result.get('products'):
        print("Artık kitap yok veya ürün bulunamadı, döngü durduruluyor.")
        break

    products = result['products']
    for product in products:
        total_products += 1
        product_group_id = product.get('productGroupId', 'Grup İd Yok')
        product_name = product.get('imageAlt', 'Name Yok')
        product_url = product.get('url', 'URL Yok')

        price = product.get('price', 'Price Yok')
        original_price = price['originalPrice']
        rating_score = product.get('ratingScore', {})
        averageRating = rating_score.get('averageRating', 'averageRating Yok')
        totalCount = rating_score.get('totalCount', 'totalCount Yok')

        try:
            averageRating_float = float(averageRating)
            averageRating_str = f"{averageRating_float:.1f}"
        except (ValueError, TypeError):
            averageRating_str = "Yok"

        if product_url != 'URL Yok':
            full_url = f"https://www.trendyol.com{product_url}"
        else:
            full_url = "URL Yok"

        # ❗ averageRating değil, averageRating_str yazılmalı
        print(f"{total_products}.{product_name} -- {original_price}TL {averageRating_str} Rating - {totalCount} Değerlendirme -- {full_url}")
        excel_datas.append({
            "name": product_name,
            "price": original_price,
            "averageRating_str": averageRating_str,
            "totalCount": totalCount,
            "url": full_url,
        })
    params['pi'] += 1
    
print(f"Toplam çekilen ürün sayısı: {total_products}")

df = pd.DataFrame(excel_datas)
df.to_excel('trendyol.xlsx', index=False)
print("\n Veriler Excel dosyasına kaydedildi: trendyol.xlsx")    


#hatalı
# i =0
# for product_link in product_links:
#     response = requests.get(url=product_link,headers=headers, cookies=cookies,timeout=15)
#     if response.status_code != 200:
#         print(f"Sayfa  erişim hatası: {response.status_code}")
#         break

    # i+=1
    # tree = html.fromstring(response.content)
    #
    # other_sellers_div = tree.xpath('//div[@class="pr-omc"]')
    #
    # if other_sellers_div:
    #     other_sellers_items = other_sellers_div[0].xpath('.//div[@class="pr-mc-w"]')
    #
    #     if other_sellers_items:
    #
    #       for other_seller in other_sellers_items:
    #           name = other_seller.xpath('.//a[@class="seller-name-text"]/text()')
    #           price = other_seller.xpath('.//span[@class="prc-dsc"]/text()')
    #
    #           seller_name = name[0].strip() if name else "Adı Bilinmiyor"
    #           seller_price = price[0].strip() if price else "Fiyatı Bilinmiyor"
    #
    #           print(f"{i}.{seller_name}-{seller_price}TL- - {product_link}")
    #
    #     else:
    #         other_sellers_items ='İtems satıcı yok'
    #
    # else:
    #     other_sellers_div ='Div başka satıcı yok'





