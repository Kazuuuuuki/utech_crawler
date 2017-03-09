# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class QiitaLikesSpider(CrawlSpider):
    name = 'qiita_likes'
    allowed_domains = ['http://qiita.com/']
    start_urls = ['http://http://qiita.com//']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse(self, response):
        page = response.url.split("/")[-1]
        filename = '../articles/qiita-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        scrap_links = ScrapLinks(response.url)
        for url in scrap_links.output():
            yield scrapy.Request(url=url, callback=self.parse)

