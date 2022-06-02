import sys
li=[]
c=0
for line in sys.stdin:
    a=eval(line)
    view=a[0]
    rd=a[1]
    view=int(view)
    if c<10:
        li.append([view,rd])
        c+=1
    else:
        mi=10**9
        for i in range(10):
            mi=min(mi,li[i][0])
        if mi<view:
            y=0
            for i in range(10):
                if li[i][0]==mi:
                    li.pop(i)
                    y=1
                    break
            if y==1:
                li.append([view,rd])
li.sort(reverse=True)
for i in range(10):
    print('The row index',li[i][1],'with',li[i][0],'views is the',i+1,'most viewed post')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   # this is the alternate code and it take the same time 
    '''li.append([view,rd])
li.sort(reverse=True)
for i in range(10):
    print('The row index',li[i][1],'with',li[i][0],'views is the',i+1,'most viewed post')'''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    

