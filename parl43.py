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
    tbl_count: int = 0
    count: int = 0
    with open(html_filename, 'rt') as h, open(csv_filename, 'wt') as c:
        for tbl in h.readlines():
            tbl_count = tbl_count + 1
            matches = re.finditer(regex, tbl)

            if matches is not None:
                for m in matches:
                    c.write(f'{m.group(1)}\n')
                    count = count + 1

        print(f"There were {tbl_count} tables found")
        print(f'There were {count} members found')



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
