from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CrawlingSpider(CrawlSpider):
    name = "webcrawler"
    allowed_domains = ["toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]
    rules = (
        Rule(LinkExtractor(allow="catalouge/category")),
        Rule(LinkExtractor(allow="catalouge", deny="category"), callback="parse_item")
    )

    def parse_item(sef, response):
        yield{
            "title": response.css(".product_main h1::text").get(),
            "price": response.css(".price_color::text").get(),
            "availability": response.css(".availability::text")[1].get().replace("/n", "").replace(" ", "")
        }
