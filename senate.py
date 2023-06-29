import re
import csv
from datetime import date

htmlfile = 'senate.html'
csvfile = 'senate.csv'
count = 0

pattern2 = '(<td[>\s].*?<\/td>)'
name_wiki = r'<td><span.data-sort-value=\"(.*?)\"><span.+?href=\"(.+?)\"'
pattern4 = '<td>(.*?)<\/td>'
pattern5 = '<td>.*?(Nunavut|Newfoundland and Labrador|Prince Edward Island|New Brunswick|British Columbia|Manitoba|Nova Scotia|Quebec|Ontario|Yukon|Alberta|Saskatchewan|Northwest Territories).*?<\/td>'
pattern6 = '<td>.*?>(.*?)<.*?<\/td>'
extract_td =  r'^<td>(.+?)<\/td><td>(.+?)<\/td><td>(.+?)<\/a><\/td><td>(.+?)<\/span><\/td><td .+?<a href=.+?>(.+?)<\/a><\/td><td>'

def import_current_members_html():
    with open(htmlfile, "rt") as h, open(csvfile, "wt") as csv
        for tr in h.readlines():
            count = count + 1
            if count > 1:


                name = ""
                wiki = ""
                party = ""
                province = ""
                appointed = ""
                m = None
                nominator = ""
                retirement = ""
                gg = ""

                # senator name and wiki link
                m = re.match(name_wiki, tr)
                if m is not None:
                    name = m.group(1)
                    wiki = m.group(2)
                else:
                    print("match was not made for the name and wiki")

                # party name
                m = re.match(self.pattern4, td.group(1))
                if m is not None:
                    party = m.group(1)
                else:
                    print("match was not made (party)")





 def getGG(self, appointedDate):
        y = date(appointedDate)
        simon = date(2021, 7, 26)

if __name__ == '__main__':
    import_current_members_html()


# copyied from senate_spider

    # rows = re.search(self.pattern1, tbl)

    """
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
                    m = re.match(self.pattern3, td.group(1))
                    if m is not None:
                        name = m.group(1)
                        wiki = m.group(2)
                    else:
                        print("match was not made")

                if count == 3:
                    m = re.match(self.pattern4, td.group(1))
                    if m is not None:
                        party = m.group(1)
                    else:
                        print("match was not made (party)")
                if count == 4:
                    m = re.match(self.pattern5, td.group(1))
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
                        print("match was not made (retirement)")

            # f.write(f"{name}\t{wiki}\t{party}\t{province}\t{appointed}\t{nominator}\t{retirement}\n")
            
            
            """
