import requests
from lxml import html

# | Sembol | Anlamı                                  | Örnek                                              |
# | ------ | --------------------------------------- | -------------------------------------------------- |
# | `/`    | Doğrudan çocuk seçimi (root’dan başlar) | `/html/body/div` → html içindeki body içindeki div |
# | `//`   | Herhangi bir derinlikteki alt öğe       | `//div` → sayfadaki tüm divler                     |
# | `.`    | Şu anki node (element)                  | `.`                                                |
# | `..`   | Bir üst node (ebeveyn)                  | `..`                                               |
# | `@`    | Attribute seçmek için                   | `//@class` → tüm class attribute’ları              |

# 1. Bütün <div> elementlerini seçmek
# //div

# 2. Belirli bir id’ye sahip element
# //div[@id='main']

# 3. Birden fazla attribute ile seçmek (class ve id örneği)
# //a[@class='link' and @href='/home']

# 4. Belirli bir index’teki element (örneğin 3. div)
# //div[3]

# *5. Elementin text içeriğini almak*
# //h1/text()

# 6. Attribute almak (örneğin bir <a> tagındaki href)
#//a/@href

#Attribute içinde kelime aranması (genelde class için):
# //div[contains(@class, 'container')]          => <div id="main" class="container">

# Birden fazla attribute’lu seçim:
# //a[@href='/home' and contains(@class, 'link deneme')]  => <a href="/home" class="link deneme">

# | XPath                  | Anlamı                                                                              | Örnek                                           |
# | ---------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------- |
# | `child::div`           | Şu anki düğümün çocukları arasında `div` olanları seçer.                            | `child::div` aynı şey `div` demek (kısa yazımı) |
# | `parent::node()`       | Şu anki düğümün ebeveynini seçer.                                                   | `parent::node()`                                |
# | `ancestor::div`        | Şu anki düğümün üst atalarından (parent, grandparent vs) `div` elementlerini seçer. | `ancestor::div`                                 |
# | `following-sibling::p` | Şu anki düğümden sonra gelen kardeş `p` elementlerini seçer.                        | `following-sibling::p`                          |
# | `attribute::class`     | Şu anki düğümün `class` attribute'unu seçer.                                        | `attribute::class` (kısa: `@class`)             |


html_content = '''
<html>
  <body>
    <div id="main" class="container">
      <h1>Başlık</h1>
      <a href="/home" class="link">Anasayfa</a>
      <a href="/about" class="link">Hakkında</a>
    </div>
  </body>
</html>
'''
tree = html.fromstring(html_content)
titles = tree.xpath('/book[price>35]/title/text()')

#1. Tüm <a> linklerini seçmek ve href attribute’unu almak
links = tree.xpath('//a/@href')
print(links)

# 2. Belirli bir class’a sahip <a> etiketini seçmek:
wanted_link = tree.xpath('//a[@class="link"]/text()')
print(wanted_link)

# 3. <h1> tag’ının text içeriğini almak  =>
# //li[1]       # tüm li'lerin ilkini
# (//li)[1]     # sayfadaki ilk li’yi
# //ul/li[1]    # her ul içindeki ilk li’yi
h1 = tree.xpath('//h1[1]/text()')  #xpath de dizinler 1 den başlar 0 dan değil unutma (//h1)][1] sayfadaki ilk h1 i alır
print(h1)
tree.xpath('(//h1//a)[2]/text()')  # 2. a alır !!!!() koymamız lazım indeks varsa (//a)[2]

#4. <div> elementinin id attribute’unu almak
div_id = tree.xpath('//div/@id')[0]
print(div_id)

#5. Bir elementin üst parent (ebeveyn) elementine gitmek
a_element = tree.xpath('//a')[0]   # İlk <a> elementi
parent_div = a_element.getparent()
print(f"uzun olan:{parent_div.attrib['id']}")

div = tree.xpath('//a/parent::div/@id')[0]
print(f"kısa olan:{div}")

#6. Karmaşık örnek: class="container" olan div içindeki <a> elementlerinin text'leri
texts = tree.xpath("//div[@class='container']//a/text()")
print(texts)
