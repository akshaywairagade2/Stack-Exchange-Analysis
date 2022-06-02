import sys
import re
creation=re.compile(r'CreationDate="(.+)" Sco')
for line in sys.stdin:
    ti=creation.finditer(line)
    for date in ti:
        data=date.group(1)
        print([data[:13],1])
