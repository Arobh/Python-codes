num=int(input(print("Enter the number you want to find the factorial: ")))
fact=1
temp=num
while num>0:
    fact=fact*num
    num=num-1
print(fact," is the factorial value of ",temp)