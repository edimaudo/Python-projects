from scrapy.spiders import Spider
from tutsplus.items import TutsplusItem
from scrapy.http    import Request

class MySpider(Spider):
  name            = "tutsplus"
  allowed_domains = ["code.tutsplus.com"]
  start_urls      = ["http://code.tutsplus.com/"]
 
  def parse(self, response):
    titles = response.xpath('//a[contains(@class, "posts__post-title")]/h1/text()').extract()
    for title in titles:
      item = TutsplusItem()
      item["title"] = title
      yield item