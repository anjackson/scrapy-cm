# -*- coding: utf-8 -*-
import scrapy


class EthosapiSpider(scrapy.Spider):
    name = 'ethosapi'
    allowed_domains = ['services.anjackson.net']
    start_urls = ['http://services.anjackson.net/']

    def parse(self, response):
        pass
