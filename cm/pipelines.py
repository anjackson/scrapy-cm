# -*- coding: utf-8 -*-

import scrapy
from scrapy.pipelines.files import FilesPipeline

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class CmFulltextPipeline(FilesPipeline):

    # For Content Mine Items, attempt to download the PDF:
    def get_media_requests(self, item, info):
        print("GAAAAAAAA %s" % item)
        # Pass the ID to use as the folder name:
        yield scrapy.Request(item['fulltext_url'], meta = {'id': item['id']})

    # Store the PDF in the CProject layout:
    def file_path(self, request, response=None, info=None):
        # To do, use fulltext.txt/pdf or scholarly.html depending on response type:
        return "%s/fulltext.pdf" % request.meta['id']
