import scrapy
import re
from datetime import date


class SenateSpider(scrapy.Spider):
    name = "senate"
    filename_html = 'senate.html'

    columns_header = "Name\tWiki\tParty\tProvince\tAppointed Date\tNominator\tRetirement Date\tAppointed By"
    pattern0 = r'^<tbody>(.*?)<\/tbody>'
    pattern1 = r'<tr>.*?<\/tr>'
    pattern2 = '(<td[>\s].*?<\/td>)'
    pattern3 = '<td><span.*?data-sort-value=\"(.*?)\".*?href="(.*?)\".*?<\/td>'
    pattern4 = '<td>(.*?)<\/td>'
    pattern5 = '<td>.*?(Nunavut|Newfoundland and Labrador|Prince Edward Island|New Brunswick|British Columbia|Manitoba|Nova Scotia|Quebec|Ontario|Yukon|Alberta|Saskatchewan|Northwest Territories).*?<\/td>'
    pattern6 = '<td>.*?>(.*?)<.*?<\/td>'

    def start_requests(self):
        urls = [
            'https://en.wikipedia.org/wiki/List_of_current_senators_of_Canada'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        tables = response.xpath("//table/*").getall()

        with open(self.filename_html, 'wt') as f:
            tbl = tables[0]
            tbl = tbl.replace('\n', '')
            tbl = tbl.replace('\r', '')
            tbl = tbl.replace('\t', '')
            tbl = re.sub(r'>\s*?<', '><', tbl)

            match = re.match(self.pattern0, tbl)
            if match:
                rows = match.group(1)
            else:
                print('There is no match to find the table rows')
                assert False

            for tr in re.finditer(self.pattern1, rows):
                f.write(f'{str(tr[0])}\n')

        f.close()


