import sys
import re
viewpattern=re.compile(r'ViewCount="(.+)" Bod')
rowpattern=re.compile(r'row Id="(.+)" Po')
for line in sys.stdin:
    vc=0
    rd=0
    match=viewpattern.finditer(line)
    for i in match:
        vc=i.group(1)
    match=rowpattern.finditer(line)
    for i in match:
        rd=i.group(1)
    print([vc,rd])
