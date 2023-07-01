import re

regex = r'(<tr>.+?<\/tr>)'
html_filename = 'parl43.html'
csv_filename = 'parl43.csv'
td_exp = r'^<tr><td style.+?<\/td>(<td>.+?<\/td>)(<td><a.+?<\/td>)(<td><a.+?<\/td><\/tr>)$'
name_wiki_exp1 = r'<td>(<?i?>?|<?b?>)<span data-sort-value=\"(.+?)\".+?<a href=\"(.+?)\".+?>(.+?)<\/a>.+?<\/td>$'
name_wiki_epx2 = r'^<td>?<?b?><a href=\"(.+?)\"\stitle=\"(.+?)\">(.+?)<\/a>.*?<\/td>$'
partyname_wiki_exp = r'^<td><a href=\"(.+?)\"\stitle=\"(.+?)\">(.+?)<\/a>.*?<\/td>$'
district_exp = r'^<td><a href=\"(.+?)\"\stitle=\"(.+?)\">(.+?)<\/a>.*?<\/td><\/tr>'
expected_count = 338

def import_current_members_parliament43():
    count = 0
    with open(html_filename, 'rt') as h, open(csv_filename, 'wt') as c:
        for tbl in h.readlines():
            matches = re.finditer(regex, tbl, re.MULTILINE)
            count = count + 1
            if matches is not None:
                for m in matches:
                    tr = m.group(1)
                    m1 = re.match(td_exp, tr)
                    sorted_mp_name = ''
                    mp_wiki = ''
                    mp_name = ''
                    party_wiki = ''
                    party_long_name = ''
                    party_short_name = ''

                    if m1 is not None:
                        m2 = re.match(name_wiki_exp1, m1.group(1))
                        if m2 is not None:
                            sorted_mp_name = m2.group(2)
                            mp_wiki = m2.group(3)
                            mp_name = m2.group(4)
                        else:
                            m2 = re.match(name_wiki_epx2, m1.group(1))
                            if m2 is not None:
                                mp_wiki = m2.group(1)
                                sorted_mp_name = m2.group(2)
                                mp_name = m2.group(3)
                            else:
                                print('There is no match for name/wiki')
                                print(m1.group(1))
                                assert False

                        m2 = re.match(partyname_wiki_exp, m1.group(2))
                        if m2 is not None:
                            party_wiki = m2.group(1)
                            party_long_name = m2.group(2)
                            party_short_name = m2.group(3)
                            # print(f'{party_wiki}\t{party_long_name}\t{party_short_name}')

                        m2 = re.match(district_exp, m2.group(3))
                        if m2 is not None:
                            district_wiki = m2.group(1)
                            district_name = m2.group(3)
                count = count + 1
                print(count)
            else:
                print('the tr rows were not matched in the table html')



def match_tr_rows(test_str: str):

    matches = re.finditer(regex, test_str, re.MULTILINE)

    for matchNum, match in enumerate(matches, start=1):

        print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                            end=match.end(), match=match.group()))

        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1

            print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum,
                                                                            start=match.start(groupNum),
                                                                            end=match.end(groupNum),
                                                                            group=match.group(groupNum)))


if __name__ == '__main__':
    import_current_members_parliament43()
