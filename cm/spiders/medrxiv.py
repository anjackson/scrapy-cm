# -*- coding: utf-8 -*-
import scrapy
import json
from cm.items import CmItem

class MedrxivSpider(scrapy.Spider):
    name = 'medrxiv'
    allowed_domains = ['www.medrxiv.org']

    custom_settings = {
        # Medrxiv's robots.txt blocks search (but not downloads):
        "ROBOTSTXT_OBEY": False
    }

    # EThOS API specific parameters:
    query_url = "https://www.medrxiv.org/search/"

    def start_requests(self):
        # Initial query e.g. https://www.medrxiv.org/search/(virus*%20OR%20viral)%20AND%20epidemic*
        yield scrapy.Request(
            "%s%s" % (self.query_url, self.query),
            callback=self.parse_list_page
        )

    # This parses list pages, extracting links to landing pages:
    def parse_list_page(self, response):
        # Find links to landing pages:
        for link in response.css('a.highwire-cite-linked-title'):
            yield response.follow(link.attrib['href'], callback=self.parse_landing_page)

        # Look for link to next page of results:
        next = response.css('li.pager-next a')
        if next:
            yield response.follow(next.attrib['href'], callback=self.parse_list_page)

    def parse_landing_page(self, response):
        citation_id = response.css('meta[name="citation_id"]').attrib['content']
        # Look for HTML
        #fulltext = response.css('meta[name="citation_full_html_url"]')
        #if fulltext is None:
        #    # Fall back on PDF
        
        # Get PDF as HTML links seem not to work, usually.
        fulltext = response.css('meta[name="citation_pdf_url"]')
        # Get url from the element:
        fulltext_url = fulltext.attrib['content']
        yield CmItem(
            id=citation_id, 
            fulltext_url = fulltext_url,
            homepage_url = response.url
            )