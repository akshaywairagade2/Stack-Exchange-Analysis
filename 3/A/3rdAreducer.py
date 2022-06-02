import sys
dic=dict()
for line in sys.stdin:
    a=eval(line)
    tag=a[0]
    if tag in dic:
        dic[tag]+=1
    else:
        dic[tag]=1
for i in dic:
    print(i,dic[i])
