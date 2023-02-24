num=int(input(print("Enter the number: ")))
temp=num
i=0
while temp>0:
    i=i+1
    temp=temp//10
temp=num
#print(i)
sum=0
while temp>0:
    rem=temp%10
    sum=int(sum+(rem**i))
    temp=int(temp/10)
#print(sum)    
if sum==num:
    print(num,"is ") 
else: 
    print(num,"is not")       
    