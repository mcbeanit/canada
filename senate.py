import re
import csv
from datetime import date, datetime

htmlfile = 'senate.html'
csvfile = 'senate.csv'

pattern2 = r'(<td[>\s].*?<\/td>)'
name_wiki = r'<td><span.data-sort-value=\"(.*?)\"><span.+?href=\"(.+?)\"'
party_name_exp = r'<td>(.*?)<\/td>'
appointed_date_exp = r'<td><span data-sort-value=\"(.+?)\"\s.+?>(.+?)<\/span><\/td>'
province_exp = r'<td>.*?(Nunavut|Newfoundland and Labrador|Prince Edward Island|New Brunswick|British ' \
               r'Columbia|Manitoba|Nova Scotia|Quebec|Ontario|Yukon|Alberta|Saskatchewan|Northwest Territories).*?<\/td>'
pm_name_exp = r'^<td><a href=\".+?\"\stitle=\"(.+?)\">(.+?)<\/a><\/td>'
extract_td = r'^<tr>(<td.+?><\/td>)(<td><span data-sort-value=.+?<\/td>)(<td>.+?<\/td>)(<td>.+?<\/td>)(<td>.+?<\/td>)(<td>.+?<\/td>)(<td>.+?<\/td>)'


def import_current_members_html():
    count = 0
    with open(htmlfile, "rt") as h, open(csvfile, "wt") as csv_file:
        for tr in h.readlines():
            count = count + 1
            if count > 1:

                name = ''
                wiki = ''
                party = ''
                province = ''
                sortable_date = ''
                appointed_date = ''
                nominator = ''
                retirement_date = ''
                retirement_sortable_date = ''
                gg = ''

                # senator name and wiki link
                m = re.match(extract_td, tr)
                if m is not None:
                    m1 = re.match(name_wiki, m.group(2))
                    name = m1.group(1)
                    wiki = m1.group(2)

                else:
                    print("match was not made for the name and wiki")

                # party name
                m1 = re.match(party_name_exp, m.group(3))
                if m1 is not None:
                    party = m1.group(1)
                else:
                    print("match was not made (party)")

                # province
                m1 = re.match(province_exp, m.group(4))
                if m1 is not None:
                    province = m1.group(1)
                else:
                    assert False

                # appointment date: sortable date and date, e.g. 'January 1, 2013'
                m1 = re.match(appointed_date_exp, m.group(5))
                if m1 is not None:
                    sortable_date = m1.group(1)
                    appointed_date = m1.group(2)
                else:
                    print('pattern for dates was not matched')
                    print(m.group(5))
                    assert False

                # prime minister nominating
                m1 = re.match(pm_name_exp, m.group(6))
                if m1 is not None:
                    nominator = m1.group(1)
                else:
                    print('pattern for PM name not matched')
                    assert False

                # retirement date
                m1 = re.match(appointed_date_exp, m.group(7))
                if m1 is not None:
                    retirement_sortable_date = m1.group(1)
                    retirement_date = m1.group(2)

                gg = get_gg(appointed_date)

                csv_file.write(
                    f'{name}\t{wiki}\t{party}\t{sortable_date}\t{appointed_date}\t{province}\t{sortable_date}\t{appointed_date}\t{nominator}\t{gg}\t{retirement_date}\n')

        print(f'There were {count - 1} active members found')


def get_gg(appointed_date: str):
    # y = date(appointedDate)
    simon_start = datetime(2021, 7, 26)

    payette_start = datetime(2017, 10, 2)
    payette_end = datetime(2021, 1, 22)

    johnston_start = datetime(2010, 10, 1)
    johnston_end = datetime(2017, 10, 2)

    jean_start = datetime(2005, 9, 27)
    jean_end = datetime(2010, 10, 1)

    wagner_start = datetime(2021, 6, 22)
    wagner_end = datetime(2021, 9, 22)

    # October 7 1999  September 27 2005
    clarkson_start = datetime(1999, 10, 7)
    clarkson_end = datetime(2005, 9, 27)

    dt = datetime.strptime(appointed_date, '%B %d, %Y')

    if dt >= simon_start:
        return 'Mary Simon'

    if payette_start <= dt <= payette_end:
        return 'Julie Payette'

    if johnston_start <= dt <= johnston_end:
        return 'David Johnston'

    if jean_start <= dt <= jean_end:
        return 'Michaelle Jean'

    if wagner_start <= dt <= wagner_end:
        return 'Richard Wagner'

    if clarkson_start <= dt <= clarkson_end:
        return 'Adrienne Clarkson'

    print(f'Appointed date not handled: {appointed_date}')
    assert False

    return 'unknown'


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
