import sys
import re
userpatternT=re.compile(r'UserId="(.+)" Text')
userpatternC=re.compile(r'UserId="(.+)" Comment')
repupattern=re.compile(r'Reputation="(.+)" Creation')
userpattern=re.compile(r'row Id="(.+)" Reputation')
posthistoryID_pattern=re.compile(r'PostHistoryTypeId="(.+)" Post')
posthistoryID=''
distri=dict()
rowT=''
rowC=''
row=''
z=0
repo=''
user=''
c=0
for line in sys.stdin:

    matchrepu=repupattern.finditer(line)
    for match in matchrepu:
        repo=match.group(1)
    matchrow=userpattern.finditer(line)
    for match in matchrow:
        user=match.group(1)
    #distri[row]=[repo,0]
    try:
        #print([row,int(repo)])
        distri[user]=[int(repo),0]
        #print(user,repo)
        
    except:
        pass
        
    usermatch=userpatternT.finditer(line)
    for match in usermatch:
        rowT=match.group(1)
    usermatch=userpatternC.finditer(line)
    for match in usermatch:
        rowC=match.group(1)
    posthistory_match=posthistoryID_pattern.finditer(line)
    for match in posthistory_match:
        posthistoryID=match.group(1)
        
    if rowT!='' and rowC!='':
        if len(rowT)<len(rowC):
            row=rowT
        else:
            row=rowC
    elif rowT=='':
        row=rowC
    else:
        row=rowT
    #print(row)
    try:
        if row in distri:
            if posthistoryID=='2':
                c+=1
                li=distri[row]
                li[1]+=1
                #print(distri[row])
    except:
        pass
z=0
for i in distri:
    li=distri[i]
    print([int(li[0]),int(li[1])])
    z+=int(li[1])
print(c,z)   
        
        
