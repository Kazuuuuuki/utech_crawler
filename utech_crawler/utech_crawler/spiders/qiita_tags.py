# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class QiitaTagsSpider(CrawlSpider):
    name = 'qiita_tags'
    allowed_domains = ['http://qiita.com/']
    start_urls = 'http://http://qiita.com/tags/'
    tags = ["機械学習", "TensorFlow", "自然言語処理", "DeepLearning"]
    pages = [85, 34, 20,49]
    for tag in tags:
        yield scrapy.Request(url=start_url + tag + "/likes", callback=self.parse)


    def parse(self, response):
        filename = 'crawl_links.txt'
        with open(filename, 'wb') as f:
            f.write(response.body)
        scrap_links = ScrapLinks(response.url)
        for url in scrap_links.output():
            yield scrapy.Request(url=url, callback=self.parse)

