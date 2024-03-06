import scrapy

class ReplicationSpider(scrapy.Spider):
    name = "replication"
    allowed_domains = ["frenify.com"]
    start_urls = ["https://frenify.com/work/envato/frenify/html/techwave/1/index.html"]

    def parse(self, response):
        print(response.body)
        pass
