# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CmItem(scrapy.Item):
    # An identifier for each item, used to make a folder to contain the results
    id = scrapy.Field()
    # The 'homepage' for the item:
    homepage_url = scrapy.Field()
    # The URL of the full-text, to download:
    fulltext_url = scrapy.Field()
