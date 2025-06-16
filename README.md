# !!!! Bu proje yalnızca eğitim ve kişisel öğrenme amacıyla oluşturulmuştur.Herhangi bir ticari amaç güdülmemiştir veya veri saklama amacı taşımaz
# WebScrapingProjects
1.BeaitfulSoap => Amazon <br>
2.Selenium => Yurtlar Burda -- **Trendyol** <br> 
3.Scrapy => <br>

# BeatifulSoap 
<h4>- - - Amazon- - - </h4>
BeatifulSoap kullanrak Amazondaki bilgisayar productlarının bilgilerini(Marka,Renk,Ram hafızası,Link) sayfa içi ve prduct içinde gezinerek gerçekleştiren ve excele kaydeden python kodu. <br>
Filtrelerin seçili olan bir url'ye istek attım.Sistem beni bot zannettiği için tüm verileri sağlıklı alamıyordum eksik ve yanlış çıkıyordu o yüzden bir header tanımladım beni gerçek bir insan gibi görmesi için.Scraping adında bir fonksiyon tanımladım burada bilgisayarların gerekli bilgilerini scraping ediyordu(Marka,Renk,Ram hafızası,Link).Sonrada while döngüsü ile tüm dış sayfaların gezdim her sayfa da scraping yapması içinde scraping fonksiyonunu çağırdım.Eğer sonraki buton yoksa dur varsa sayfa numarasını arttır.<br>

# Selenium 
<h4>- - - Trendyol- - - </h4>
Trendyolun ana url'sinden yola çıkarak gerekli reklamları kapatır, çerezleri kabul eder , input kısmına ayakkabı komutunu gönderir ve yeni url'ye gider.Devamında ise marka ve numara seçer(nike,22 numara).
Sonrasındaysa sayfayı scroll eder.Artık tüm ürünleri ekranda görmüş olduk doğruluk tespiti için scroll sonrası ürün sayısını aldım test için. Şimdi artık ürünlerimizin hepsi hazır scraping işlemi kaldı.Ürünlerin linklerini de bir listeye attım o listeden çektim sayfalara tek tek gittim ve gittiğim sayfadan ürünlerin ismini aldım. Hem o sayfadaki fiyatı hem de rakip satıcıdaki fiyatı ve mağaza adını aldım.Excel dosayasını da ekledim.<br><br>
<h7>Ekran Çıktısı</h7> <br>
187 - - - Scroll edildikten sonra toplam ürün sayısı: 187 <br><br>
-1.Nike Bebek Günlük Ayakkabı DV5458-105 Beyaz--1.999 TL   =>>    https://www.trendyol.com/nike/bebek-gunluk-ayakkabi-dv5458-105-beyaz-p-836891634?boutiqueId=61&merchantId=856203<br>
Rakip Mağaza Adı:Munesso - Fiyatı:1.999 - Linki:https://www.trendyol.com/sr?mid=381713<br><br>
2.Nike Bebek Günlük Ayakkabı DV5458-104 Beyaz ve 1.999TL ,https://www.trendyol.com/nike/bebek-gunluk-ayakkabi-dv5458-104-beyaz-p-836891545?boutiqueId=61&merchantId=381713 ->için başka satıcı yok<br>
<h4>- - - YurtlarBurda- - - </h4>
Yurt ararken en çok kullandığım sitelerden biri olmuştu ve bende düşünüp dedimki neden yurtların verilerini çekmeyeyim.Öncelikle klasık bir arama işlemi yapıyoruz gerekli filtreleri seçtik.Tüm elemntleri sayfada görmek için en altta bulunan "daha fazla gör" butonuna click yaptık.Sonra tüm kartları aldım ve her bir kart için döngü(for) oluşturdum.İstedeğim yurtlarda {'Şişli', 'Fatih', 'Kağıthane', 'Beşiktaş'} bu illerdeki yurtlardı o yüzden kendimce böyle bir filtre oluşturdum sadece bu illerdeki yurtların bilgilerini getirsin.Bazılarının ilçesi belli değildi o yüzden bir "," ile if işlemi tanımladım.Sonrada bu ilçedeki yurtları bir listeye attım url ve ilçesiyle birlikte. Devamındaysa listedeki yurtlara get(url) ile sayfalara gittim.Yurt adını, yatak sayısını,öğün sayısını,adresi ve telefon numarasını aldım ve bunları bir excel dosyasına da kaydettim.<br>

# Scrapy
<h4>- - - gelecek.... - - </h4>

