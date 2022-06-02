import sys
import subprocess
c=0
x=0
y=0
xy=0
x2=0
y2=0
co=0
#subprocess.call('read -t 30', shell=True)
for line in sys.stdin:
    aa=eval(line)
    a=int(aa[0])
    b=int(aa[1])
    '''try:
        a=int(a)
    except:
        pass
    try:
        b=int(b)
    except:
        pass'''
    x+=a
    y+=b
    xy+=a*b
    x2+=a**2
    y2+=b**2
    c+=1
#print(c,x,y,xy,x2,y2)
co=float(c*xy-x-y)/float(((c*x2-x**2)*(c*y2-y**2))**(0.5))
print("The correlation coefficient of the reputation of the user in Users.xml to the total answers given by the user in PostsHistory.xml file is ",co)
