import sys
li=[]
month=None
c=1
nowmonth=None
le=0

for line in sys.stdin:
    a=eval(line)
    month=a[0]
    le=a[1]
    year=a[2]
    le=int(le)
    
    
    if month!=nowmonth:
        if nowmonth==None:
            nowmonth=month
            c=1
        else:
            li.sort()
            #med=li[c//2]
            if len(li)>0:
            
                print("The median of month",month,"year",year,"is",li[len(li)//2])
            
    	        #print(month,li) 
    	        #print(len(li),li[len(li)//2])
                #print(c)
                
            nowmonth=month
            
            li=[]
            c=1
    else:
        li.append(int(le))
        c+=1
li.sort()
#med=li[c//2]
#print(f'The median is {li}') 
