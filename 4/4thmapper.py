import sys
import re
textpattern=re.compile(r'Text="(.+)" Crea')
datepattern=re.compile(r'CreationDate=(.+)" Use')
le=0
month=0
year=0
for line in sys.stdin:
    matchestext = textpattern.finditer(line)
    matchesdate=datepattern.finditer(line)
    for match in matchestext:
        data = match.group(1)
        le=len(data)
    for match in matchesdate:
        data = match.group(1)
        data=data.split("-")
        month=data[1]
        year=data[0]
    print([month,le,year])
