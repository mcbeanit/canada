import scrapy
import re
import string


class CanadaDistrictsSpider(scrapy.Spider):
    name = 'CanadaDistrictsSpider'
    expected_count = 338

    def start_requests(self):
        urls = ['https://en.wikipedia.org/wiki/List_of_Canadian_electoral_districts']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        ul = response.xpath("//ul/li").getall()
        if ul is None:
            assert False
        with open('tmp.html', 'wt',  encoding='utf-8') as h:
            for i in range(132, 470):
                li = ul[i]
                li = li.replace('\n', '')
                li = li.replace('\r', '')
                li = li.replace('\t', '')
                li = ''.join(c for c in li if c.isprintable())
                h.write(f'{li}\n')
