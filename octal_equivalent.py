num=int(input('Enter the number: '))
sum=0
k=1
while num>0:
    a=num%8
    num=num//8
    sum+=a*k
    k=k*10
print(sum)    