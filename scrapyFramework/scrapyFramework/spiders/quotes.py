# -*- coding: utf-8 -*-
import scrapy
from ..items import ScrapyframeworkItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com/']
    # start_urls = ['http://quotes.toscrape.com/page/1/']

    def __init__(self, page=None, *args, **kwargs):
        super(QuotesSpider, self).__init__(*args, **kwargs)
        if isinstance(page, str):
            self.start_urls = [
                'http://quotes.toscrape.com/page/%s/' % page
            ]
            self.page = page

    def parse(self, response):
        for quote in response.css('div.quote'):  # 写一个for循环去遍历，每次提取一个elem，使用css选择器去定位元素。
            elem = ScrapyframeworkItem()
            elem["text"] = quote.css("span.text::text").extract_first()
            elem["author"] = quote.css("small.author::text").extract_first()
            elem["tags"] = quote.css("div.tags a.tag::text").extract()
            yield elem
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse, dont_filter=True)

        filename = "source.html"
        with open(filename, "wb") as f:
            f.write(response.body)
