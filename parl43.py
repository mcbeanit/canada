import re

regex = r'(<tr>.+?<\/tr>)'
html_filename = 'parl43.html'
csv_filename = 'parl43.csv'
td_exp = r'^<tr><td style.+?<\/td>(<td>.+?<\/td>)(<td><a.+?<\/td>)(<td><a.+?<\/td><\/tr>)$'

def import_current_members_parliament43():
    with open(html_filename, 'rt') as h:
        for tbl in h.readlines():
            matches = re.finditer(regex, tbl, re.MULTILINE)
            if matches is not None:
                for m in matches:
                    tr = m.group(1)
                    m1 = re.match(td_exp, tr)
                    if m1 is not None:
                        print(m1.group(1))
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
