import scrapy
from ..items import EbayItem

class EbayDroneSpider(scrapy.Spider):
    name = "ebay_drone"
    allowed_domains = ["ebay.com"]
    start_urls = ["https://www.ebay.com/b/3DR-Camera-Drones/179697/bn_7115817505?_udlo=75&mag=1&_udhi=350"]

    def parse(self, response):
        product_links = list(set(response.css('a.brwrvr__item-card__image-link::attr(href)').getall()))
        print(f"Sayfa URL: {response.url} - Ürün linkleri sayısı: {len(product_links)}")
        for link in product_links:
            print(f"Ürün linki: {link}")
            yield response.follow(link, callback=self.parse_drone)

        next_page = response.css('a.pagination__next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_drone(self, response):
        # self.crawler.stats.inc_value('product_count')

        drone = EbayItem()
        drone["name"] = response.xpath('//*[@id="mainContent"]/div[1]/div[1]/h1/span/text()').get(default="")
        drone["price"] = response.xpath('//*[@id="mainContent"]/div[1]/div[3]/div/div/div[1]/span/text()').get(default="").strip()
        drone["seller_name"] = response.xpath('//*[@id="mainContent"]/div[1]/div[2]/div/div[1]/div/div[2]/div[1]/a/span/text()').get(default="").strip()
        drone["url"] = response.url

        yield drone

