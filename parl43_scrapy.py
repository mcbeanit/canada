import scrapy
import re


class QuotesSpider(scrapy.Spider):
    name = "parl"
    expected_count = 338

    def start_requests(self):
        urls = [
            'https://en.wikipedia.org/wiki/List_of_House_members_of_the_43rd_Parliament_of_Canada'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        pattern1 = '^<td>.*?<a\shref=\"(.*?)\"\stitle=.*?>(.*?)<'
        pattern2 = '^<td>(Conservative|Liberal|New Democratic|Green|Bloc Québécois)'
        # ^<tr><td.*?<a\shref=\"(\/wiki.*?)\"\stitle=.*?>(.*?)<

        l = response.xpath("//tr").getall()
        filename = 'parl.html'
        with open(filename, 'wt') as f:
            for n in l:
                n = n.replace('\n', '')
                n = n.replace('\r', '')
                n = n.replace('\t', '')
                n = re.sub('\u2003', '', n)
                n = re.sub('\u2212', '', n)
                n = re.sub('\uc2a0', '', n)
                n = re.sub(r'>\s+?<', '><', n)

                f.write(f'{n}\n')

                '''
                m = re.search(pattern1, n)
                if m is not None and len(m.groups()) > 0:
                    f.write(f"{m.group(1)}\t{m.group(2)}\n")

                m = re.search(pattern2, n)
                if m is not None and len(m.groups()) > 0:
                    f.write(f"{m.group(1)}\n")
                '''