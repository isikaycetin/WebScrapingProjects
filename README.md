# !!!! Bu proje yalnızca eğitim ve kişisel öğrenme amacıyla oluşturulmuştur.Herhangi bir ticari amaç güdülmemiştir veya veri saklama amacı taşımaz
# WebScrapingProjects
1.BeaitfulSoap => Amazon <br>
2.Selenium => Yurtlar Burda -- **Trendyol** - Akakçe<br> 
3.Scrapy => Ebay <br>
4.lxml + requests => Uspolo <br>
5.Hidden Api + requests => eBooks <br>

# Hidden Api-Emulate


# Lxml
<h4>- - - Uspolo- - - </h4>
Lxml kullanarak Uspolo sitesindeki tişörtlerin adını,fiyatını,url'sini excel dosyasına kaydeden python kodu.Öncelikle bir ana urlmiz var ve url içinde page parametresi sayfa sayfa gezinmek için paramktereyi +1 attrıdık eğer artık ürün yoksa yeni sayfa demekki o sayfaf yok aslında dur.scraping_products(products) adındaki methodumuzda her tişörtün linkini alır ana url'ye ekle xpath de sonuç hep liste olarak döner bir tane olsa bile o yüzden [0] kullanmamız lazım.Sonra da name,price ve url xpath ile scrape ettim ve excel'e kaydeder.<br>

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
<h4>- - - Akakçe - - </h4>
Bu web sitesindeki kod trendyoldaki koda benzer ancak daha clean bir kod yazmayı amaçladım daha işlevsel fonksiyonlar kullandım.Alınan datalar ise product adı,fiyatı ve linki => rakip fiyatı ve linki. Önce yine bir url var ve url ye gidiyoruz while döngüsünün içine girip önce her sayfadaki veriyi kazıyoruz sonra diğer sayfalara click ile geçiyoruz.Trendyoldan farklı olarak sayfa döngüsü içine 2 tane fonksiyon ekledim biri productların linklerini listeye ekliyor diğeride o linklere gidip dataları scraping ediyor.En son olarakta kontrol işlemleri için print kullanıyorum ve excel dosyasına kaydediyorum.** İleriki kısımda sitede de bulunan fiyat analizi kısımlarını da ekleme düşüncem var ** <br>

# Scrapy
<h4>- - - Ebay - - </h4>
Ebayden dronelerin adını,fiyatını,mağaza adını ve linki bulmak istedim ama her şey doğru olmasına rağmen json dosyasında bazılarının ismi var bazılarının fiyatı var karışık oldu o yüzden onu atmadım çok uğraştım ama çözemedim her şey doğru xpathler linkler.<br>
Öncelikle items.py'ye field() alanlarını ekledik hangi dataları almak istiyorsak.Sonrada settings.py'ye headers ekledim ve ROBOTSTXT_OBEY = False olarak ayarladım yoksa beni bot sanıyor site.
spider'ın içine giricek olursak main kodların olduğu kısım, öncelikle bir seçili fitrelerin olduğu url var.Bu url de dronler var.İlk olarak sayfadaki productların linklerini aldık.Bu linklere tek tek parse_drone fonksiyonuna yolladık.Tüm sayfaları almak içinde tekrar parse fonksiyonuna gittik recursive bir yapıya benzer bir yapı oluştu.Parse_drone de ise xpath ile seçtik ve yield ettik. 

