# !!!! Bu proje yalnızca eğitim ve kişisel öğrenme amacıyla oluşturulmuştur.Herhangi bir ticari amaç güdülmemiştir veya veri saklama amacı taşımaz
# WebScrapingProjects
1.BeaitfulSoap - Amazon <br>
2.Selenium - Yurtlar Burda - **Trendyol** <br> 
3.Scrapy  <br>

# BeatifulSoap 
BeatifulSoap kullanrak Amazondaki bilgisayar productlarının bilgilerini(Marka,Renk,Ram hafızası,Link) sayfa içi ve prduct içinde gezinerek gerçekleştiren python kodu. <br>
# Selenium 
<h4> 1.Trendyol </h4>
Trendyolun ana url'sinde yola çıkarak gerekli reklamları kapatır, çerezleri kabuş eder , input kısmına ayakkabı komutunu gönderir ve yeni url'ye gider.Devamında ise marka ve numara seçer(nike,22 numara).
Sonrasındaysa sayfayı scroll eder.Artık tüm ürünleri ekranda görmüş olduk doğruluk tespiti için scroll sonrası ürün sayısını aldım test için. Şimdi artık ürünlerimizin hepsi hazır scraping işlemi kaldı.Ürünlerin linklerini de bir listeye attım o listeden çektim sayfalara tek tek gittim ve gittiğim sayfadan ürünlerin ismini aldım. Hem o sayfadaki fiyatı hem de rakip satıcıdaki fiyatı ve mağaza adını aldım.Excel dosayasını da eklediim.<br>
<h7>Ekran Çıktısı</h7> 
187 - - - Scroll edildikten sonra toplam ürün sayısı: 187 <br>
-------------1.Nike Bebek Günlük Ayakkabı DV5458-105 Beyaz--1.999 TL------https://www.trendyol.com/nike/bebek-gunluk-ayakkabi-dv5458-105-beyaz-p-836891634?boutiqueId=61&merchantId=856203----<br>
Mağaza Adı:Munesso - Fiyatı:1.999 - Linki:https://www.trendyol.com/sr?mid=381713<br>
2.Nike Bebek Günlük Ayakkabı DV5458-104 Beyaz ve 1.999TL ,https://www.trendyol.com/nike/bebek-gunluk-ayakkabi-dv5458-104-beyaz-p-836891545?boutiqueId=61&merchantId=381713 ->için başka satıcı yok<br>

-------------3.Nike Unisex Bebek Beyaz Bq5453-100 Court Borough Low Spor Ayakkabı--2.219 TL------https://www.trendyol.com/nike/unisex-bebek-beyaz-bq5453-100-court-borough-low-spor-ayakkabi-p-34757167?boutiqueId=61&merchantId=302224----<br>
Mağaza Adı:BULUTSPOR - Fiyatı:2.197 - Linki:https://www.trendyol.com/sr?mid=758666<br>
Mağaza Adı:ABSPOR - Fiyatı:2.199 - Linki:https://www.trendyol.com/sr?mid=791549<br>
Mağaza Adı:NAZSPOR - Fiyatı:2.229 - Linki:https://www.trendyol.com/sr?mid=686130<br>
Mağaza Adı:GLR SPOR - Fiyatı:2.289 - Linki:https://www.trendyol.com/sr?mid=730585<br>




