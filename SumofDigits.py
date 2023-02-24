num=int(input(print("Enter a 5 digit number: ")))
sum=0
'''
sum=int(sum+num%10)
print(sum)
num=num/10
sum=int(sum+num%10)
print(sum)
num=num/10
sum=int(sum+num%10)
print(sum)
num=num/10
sum=int(sum+num%10)
print(sum)
num=num/10
sum=int(sum+num%10)
print(sum)
print("Sum of digits = ",sum)
'''
while num>0:
    sum=int(sum+num%10)
    num=num/10
print("Digits sum = ",sum)    