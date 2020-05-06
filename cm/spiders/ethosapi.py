# -*- coding: utf-8 -*-
import scrapy
import json
from cm.items import CmItem

class EthosapiSpider(scrapy.Spider):
    name = 'ethosapi'
    allowed_domains = ['services.anjackson.net']

    # EThOS API specific parameters:
    query_url = "https://services.anjackson.net/ov/solr/discovery/select"
    # default query parameters (attempt to return all matching rows by default):
    rows = 999999 
    query_field = 'text'

    def start_requests(self):
        # Set up query parameters, with 'query' passed as a command-line argument:
        params = {
            'q': self.query,
            'df': 'text',      # This field contains the text to search.
            'rows': str(self.rows)  # How many matches to return
        }
        # Initial query does a POST
        yield scrapy.FormRequest(
            self.query_url,
            callback=self.parse,
            method='POST',
            formdata=params
        )

    def parse(self, response):
        data = json.loads(response.body_as_unicode())
        num_found = data['response']['numFound']
        self.logger.info("Query '%s': %i hits." %(self.query, num_found) )
        for hit in data['response'].get('docs', []):
            # Strip prefix off EThOS ID:
            ethos_id = hit['id'].replace('ethos:','')
            yield CmItem(
                id=ethos_id, 
                fulltext_url = hit['url'][0],
                homepage_url = hit.get('ethos_url_s', '')
                )