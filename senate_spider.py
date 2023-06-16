import scrapy
import re
from datetime import date

class SenateSpider(scrapy.Spider):
    name = "senate"
    pattern1 = '<tr>.*?<\/tr>'
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

        l = response.xpath("//table/*").getall()
        filename = 'senate.html'
        with open(filename, 'wt') as f:
           f.write("Name\tWiki\tParty\tProvince\tAppointed Date\tNominator\tRetirement Date\tAppointed By") 
           tbl = l[0]
           tbl = tbl.replace("\n","")
           rows = re.search(self.pattern1,tbl)
           if rows is None:
               f.write("There were no matches\n")
           else:
               for tr in re.finditer(self.pattern1, tbl):
                   count = 0
                   name = ""
                   wiki = ""
                   party = ""
                   province = ""
                   appointed = ""
                   m = None
                   nominator = ""
                   retirement = ""
                   gg = ""

                   for td in re.finditer(self.pattern2, tr.group(0)):
                       count += 1
                       if count == 2:
                           m = re.match(self.pattern3,td.group(1))
                           if m is not None:
                               #print(m.groups())
                               name = m.group(1)
                               wiki = m.group(2)
                           else:
                               print("match was not made")

                       if count == 3:
                           # f.write(f"{td.group(0)}\n")
                           m = re.match(self.pattern4,td.group(1))   
                           if m is not None:
                               party = m.group(1)
                           else:
                               print("match was not made (party)") 
                       if count == 4:
                          
                           m = re.match(self.pattern5,td.group(1))       
                           if m is not None:
                               province = m.group(1)
                           else:
                               print("match was not made (province)")
                               f.write(f"{td.group(1)}\n")
                       if count == 5:
                           m = re.match(self.pattern6, td.group(1))
                           if m is not None:
                               appointed = m.group(1)
                           else:
                               print("match was not made (appointed date)") 

                       if count == 7:
                           m = re.match(self.pattern6, td.group(1))
                           if m is not None:
                               nominator = m.group(1)
                           else:
                               print("match was not made (nominator)") 

                       if count == 8:
                           m = re.match(self.pattern6, td.group(1))
                           if m is not None:
                               retirement = m.group(1)
                           else:
                               print ("match was not made (retirement)" )          

                   f.write(f"{name}\t{wiki}\t{party}\t{province}\t{appointed}\t{nominator}\t{retirement}\n")
                   #f.write("\n")}

    
    def getGG(self, appointedDate):
        y = date(appointedDate)
        simon = date(2021,7,26)
   

				   
				   
				   
				   