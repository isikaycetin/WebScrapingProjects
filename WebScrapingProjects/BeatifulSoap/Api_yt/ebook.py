import requests
import pandas as pd

cookies = {

}

headers = {

}

params = {
    'CountryCode': 'US',
    'bisacId': '5204',
}

response = requests.get('https://www.ebooks.com/api/search/bisac/', params=params, cookies=cookies, headers=headers)
data = response.json()
# print(data.keys())  # keyleri verir
# print(data.values()) #value
# print(data.items())  #key-value

#print(len(data["books"]))

#tüm sayfaları eder ama en az 500 sayfayı görünce saldım ilk 20 sayfa yeter
# page_number=1
# while True:
#     page_url = f'https://www.ebooks.com/api/search/bisac/?pageNumber={page_number}&CountryCode=US&bisacId=5204'
#     response = requests.get(page_url, cookies=cookies, headers=headers)
#
#     if response.status_code != 200:
#         print(f"Hata oluştu. Kod: {response.status_code}")
#         break
#
#     data = response.json()
#     books = data['books']
#     if not books:
#         print("Artık kitap yok, döngü durduruluyor.")
#         break
#
#     print(f" - - - - - {page_number}.Sayfa - - - - - - - ")
#     for book in books:
#         book_id = book['id']
#         detail_url =f"https://www.ebooks.com/api/book/?bookId={book_id}&countryCode=US"
#         response = requests.get(detail_url, cookies=cookies, headers=headers)
#
#         if response.status_code == 200:
#             detail_data = response.json()
#
#             information = detail_data['information']
#             print(information.get('title', 'Başlık Yok'))
#             print(information['authors'])
#             print(information.get('publisher_name', 'Yayınevi Yok'))
#             print(information.get('long_publication_date', 'Tarih Yok'))
#
#             price = detail_data.get('price', {})
#             print(price.get('price', 'fiyat yok'))
#         print("------------------------------------ ")
#     print("- - - - - - - - - - - - - - - - - - - - - - -- - - - - - - - -- - - -  ")
#     page_number+=1

page_number = 1
max_pages = 50
total_products = 0
excel_datas = []
while page_number <= max_pages:
    page_url = f'https://www.ebooks.com/api/search/bisac/?pageNumber={page_number}&CountryCode=US&bisacId=5204'
    response = requests.get(page_url, cookies=cookies, headers=headers)

    if response.status_code != 200:
        print(f"Hata oluştu. Kod: {response.status_code}")
        break

    data = response.json()
    books = data['books']
    if not books:
        print("Artık kitap yok, döngü durduruluyor.")
        break

    print(f" - - - - - {page_number}. Sayfa - - - - - - - ")
    for book in books:
        total_products += 1
        book_id = book['id']
        detail_url = f"https://www.ebooks.com/api/book/?bookId={book_id}&countryCode=US"
        response = requests.get(detail_url, cookies=cookies, headers=headers)

        print(f"--{total_products}.book--")
        if response.status_code == 200:
            detail_data = response.json()
            information = detail_data['information']
            print(f"Ad:{information.get('title', 'Başlık Yok')}")
            print(f"Yazar:{information['authors']}")
            print(f"Yayın evi:{information.get('publisher_name', 'Yayınevi Yok')}")
            print(f"Tarih:{information.get('long_publication_date', 'Tarih Yok')}")
            price = detail_data.get('price', {})
            print(f"Fiyat:{price.get('price', 'fiyat yok')}")

            excel_datas.append({
                "Başlık": information.get('title', 'None'),
                "Yazarlar": information.get('authors', 'None'),
                "Yayın Evi": information.get('publisher_name', 'None'),
                "Tarih": information.get('long_publication_date', 'None'),
                "Fiyat": price.get('price', 'Fiyat Yok')
            })

        print(f"{total_products}. kitap kaydedildi.")
        print("------------------------------------ ")
    print("\n")
    page_number += 1

print(f"Toplam çekilen ürün sayısı: {total_products}")
df = pd.DataFrame(excel_datas)
df.to_excel("ebooks.xlsx", index=False)
print("Veriler 'ebooks.xlsx' dosyasına kaydedildi.")
