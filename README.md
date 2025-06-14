# !!!! Bu proje yalnızca eğitim ve kişisel öğrenme amacıyla oluşturulmuştur.Herhangi bir ticari amaç güdülmemiştir veya veri saklama amacı taşımaz
# WebScrapingProjects
1.BeaitfulSoap - Amazon <br>
2.Selenium - Yurtlar Burda - **Trendyol** <br> 
3.Scrapy  <br>

# BeatifulSoap 
BeatifulSoap kullanrak Amazondaki bilgisayar productlarının bilgilerini(Marka,Renk,Ram hafızası,Link) sayfa içi ve prduct içinde gezinerek gerçekleştiren ve excele kaydeden python kodu. <br>
# Selenium 
<h4> 1.Trendyol </h4>
Trendyolun ana url'sinden yola çıkarak gerekli reklamları kapatır, çerezleri kabul eder , input kısmına ayakkabı komutunu gönderir ve yeni url'ye gider.Devamında ise marka ve numara seçer(nike,22 numara).
Sonrasındaysa sayfayı scroll eder.Artık tüm ürünleri ekranda görmüş olduk doğruluk tespiti için scroll sonrası ürün sayısını aldım test için. Şimdi artık ürünlerimizin hepsi hazır scraping işlemi kaldı.Ürünlerin linklerini de bir listeye attım o listeden çektim sayfalara tek tek gittim ve gittiğim sayfadan ürünlerin ismini aldım. Hem o sayfadaki fiyatı hem de rakip satıcıdaki fiyatı ve mağaza adını aldım.Excel dosayasını da ekledim.<br>
<h7>Ekran Çıktısı</h7> 
187 - - - Scroll edildikten sonra toplam ürün sayısı: 187 <br>
-1.Nike Bebek Günlük Ayakkabı DV5458-105 Beyaz--1.999 TL   =>>    https://www.trendyol.com/nike/bebek-gunluk-ayakkabi-dv5458-105-beyaz-p-836891634?boutiqueId=61&merchantId=856203<br>
Mağaza Adı:Munesso - Fiyatı:1.999 - Linki:https://www.trendyol.com/sr?mid=381713<br>
2.Nike Bebek Günlük Ayakkabı DV5458-104 Beyaz ve 1.999TL ,https://www.trendyol.com/nike/bebek-gunluk-ayakkabi-dv5458-104-beyaz-p-836891545?boutiqueId=61&merchantId=381713 ->için başka satıcı yok<br>






