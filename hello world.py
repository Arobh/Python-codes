'''
msg='Hello world'
print(msg)
n=4
a=1
b=1
for i in range(1,n+1):
    print(end="  "*(n+1-b))
    for j in range(1,i+1):
        print(a,end="   ")
        a=a+1
    b=b+1
    print()    
'''
'''
num =int(input('Enter: '))
sum=0
i=1
while num>0:
    rem=num%8
    num=num//8
    sum=sum+rem*i
    i=i*10
print(sum)  
'''
'''
n=int(input('Enter how many: '))
#max=int(max)
#min=int(min)
list=[]
for i in list:
    list[i]=input('Enter :')
max=list[0]
min=list[0]
for i in range(0,n):
    if list[i]>max:
        max=lst[i]
    if list[i]<min:
        min=lst[i]      
print(max,min)       
''' 
n=input('Enter the numbers:').split()
max=-1000000000
min=1000000000
for i in n:
    if int(i)>int(max):
        max=i    
    if int(i)<int(min):
        min=i
print(max,min)            