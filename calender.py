'''x=(1,2,3,4,5)
y=(10,20,x,30)
print(x)
print(y)
z=(10,20,*x,30)
print(z)
'''
'''
import calendar
year=2023
month=1
x=calendar.month(year,month)
print(x)'''
def func(ALIST):
    i=0
    for i in range(0,len(ALIST)):
        
        for j in range(i+1,len(ALIST)):
            if( ALIST[i] > ALIST[j] ):
                t=ALIST[i]
                ALIST[i]=ALIST[j]
                ALIST[j]=t
                
    return ALIST  

thisalist=[1,2,32,2,7,4,5,6,7]

print(thisalist)
print(func(thisalist))