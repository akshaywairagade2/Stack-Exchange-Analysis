import sys
li=[]
lasthour=None
hour=None
c=0
for line in sys.stdin:
    a=eval(line)
    hour=a[0]
    if hour!=lasthour:
        if lasthour==None:
            lasthour=hour
            c=1
        else:
            li.append([c,lasthour])
            print('The number of posts hour',lasthour,'are',c)
            lasthour=hour
            c=1
    else:
        c+=1
print('The number of posts hour',lasthour,'are',c)
li.append([c,lasthour])
li.sort()
print("Hours in which posts are not there are not considered for calculating peak to lowest user activity per hour")


print("The ratio of the peak to lowest user activity per hour is ",li[-1][0]/li[0][0],"peak was in hour",li[-1][1],"and lowest activity was in hour",li[0][1])
   
