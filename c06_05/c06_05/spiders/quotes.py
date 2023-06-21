import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from c06_05.items import Quote


class QuotesSpider(CrawlSpider):
    # クロール実行時に指定するクローラー名
    name = "quotes"
    # クロール対象のコンテンツがホストされているドメインを制限できる
    allowed_domains = ["quotes.toscrape.com"]
    # クロールの起点となるインデックスのページのURL
    start_urls = ["https://quotes.toscrape.com"]

    rules = (
        Rule(
            LinkExtractor(allow=r"Items/"),
            callback="parse_item",
            follow=True
        ),
    )

    def parse_item(self, response):
        """
        クロールしたページからItemをスクレイピングする。
        """
        for quote_html in response.css("div.quote"):
            item = Quote()
            # item["author"] = quote_html.css("span.author::text").extract_first()
            # item["text"] = quote_html.css("span.text::text").extract_first()
            # item["tags"] = quote_html.css("div.tags a.tag::text").extract()
            item["author"] = quote_html.css("small.author::text").get()
            item["text"] = quote_html.css("span.text::text").get()
            item["tags"] = quote_html.css("div.tags a.tag::text").getall()
            yield item
