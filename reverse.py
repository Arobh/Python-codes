'''num=input(print("Enter an input: "))
print(num[-1::-1])
'''
'''
num = int(input(" enter the number: "))
while num>0:
    n=int(num%10)
    print(n)
    num=int(num/10)
'''
'''
num = int(input(" enter the number: "))
while num>0:
    print(num%10)
    num=num//10
'''
num = int(input(" enter the number: "))
temp=num
rev=0
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=int(num/10)
print(temp,"Reverse number = ",rev)    
if rev== temp:
    print(rev," is palindrome")
else :
    print(rev,"is not palindrome")    