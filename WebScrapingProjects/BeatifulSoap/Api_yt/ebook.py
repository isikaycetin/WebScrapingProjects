import requests
import pandas as pd

cookies = {
    '__cflb': '02DiuEnpWqjzEfhLpxZQz37qrxw1gPiwMqSgWDSG5iSFE',
    '_ga': 'GA1.1.1457839413.1750799007',
    '_gcl_au': '1.1.1157359609.1750799007',
    'CountryCode': 'US',
    '.AspNetCore.Antiforgery.IbIT5byLPeQ': 'CfDJ8PQEgL4qluhFn4qBpbB9vPgFySsXpzV85CczE2PoS3Y6QR1wpNuyiLit2T5dSdzqKpkJizBaHWCGBDHoc03OYGlbMC_Vn6ZtIy2lY0Wxsboa6EqEdldZ8Hwal4iknLVuw1U2BcWCD9GaGeAhYQzvNzc',
    'cf_clearance': 'MAB_.1NP6xH4c5zQ.2h4KZ1Qynn6h04FTHhwZfgIG58-1750850194-1.2.1.1-jlhHkn9EqPt3CyaUsa7YAjLFklsfcZyPXkPrpG5HGJ1XERLD9vrNui0rZGrlqcy65gPDzc32MVDiZdLv6S2VSvIEwbww7qLyL8GQm99WTwqE_qWCwWbC29sJ9LWqDX0BarUa5Nu1sW3c3xT_ANOR1RMinYH9xnfHy.mh0VVMvlO5IBnB2F_.5xSX1geka5O0Qr0NeAZ36nNfTbK8litCIYh1b5UE2AJq4CVZBzqPWce4VPI8Ryaqbtr9rKXQuMqzvc.S1DoBkhixpjznfKgivYgo1QutjVVUvCK4bWGQLUUo8Va9EFpgy5uBN9wgA5Vfhe1pS_kz.FzAbA_iUJsx7zfgtsB7RsvpmudSNxOsJDE',
    '_uetsid': 'ac276890513e11f0a327e1523129ca8a',
    '_uetvid': 'ac278be0513e11f09f58f7df84f1d39a',
    '_ga_FQMQQ21J7D': 'GS2.1.s1750848728$o2$g1$t1750850728$j16$l0$h0',
}

headers = {
    'accept': '*/*',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.ebooks.com/en-us/category/computers/5204/',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    # 'cookie': '__cflb=02DiuEnpWqjzEfhLpxZQz37qrxw1gPiwMqSgWDSG5iSFE; _ga=GA1.1.1457839413.1750799007; _gcl_au=1.1.1157359609.1750799007; CountryCode=US; .AspNetCore.Antiforgery.IbIT5byLPeQ=CfDJ8PQEgL4qluhFn4qBpbB9vPgFySsXpzV85CczE2PoS3Y6QR1wpNuyiLit2T5dSdzqKpkJizBaHWCGBDHoc03OYGlbMC_Vn6ZtIy2lY0Wxsboa6EqEdldZ8Hwal4iknLVuw1U2BcWCD9GaGeAhYQzvNzc; cf_clearance=MAB_.1NP6xH4c5zQ.2h4KZ1Qynn6h04FTHhwZfgIG58-1750850194-1.2.1.1-jlhHkn9EqPt3CyaUsa7YAjLFklsfcZyPXkPrpG5HGJ1XERLD9vrNui0rZGrlqcy65gPDzc32MVDiZdLv6S2VSvIEwbww7qLyL8GQm99WTwqE_qWCwWbC29sJ9LWqDX0BarUa5Nu1sW3c3xT_ANOR1RMinYH9xnfHy.mh0VVMvlO5IBnB2F_.5xSX1geka5O0Qr0NeAZ36nNfTbK8litCIYh1b5UE2AJq4CVZBzqPWce4VPI8Ryaqbtr9rKXQuMqzvc.S1DoBkhixpjznfKgivYgo1QutjVVUvCK4bWGQLUUo8Va9EFpgy5uBN9wgA5Vfhe1pS_kz.FzAbA_iUJsx7zfgtsB7RsvpmudSNxOsJDE; _uetsid=ac276890513e11f0a327e1523129ca8a; _uetvid=ac278be0513e11f09f58f7df84f1d39a; _ga_FQMQQ21J7D=GS2.1.s1750848728$o2$g1$t1750850728$j16$l0$h0',
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