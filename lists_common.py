a=[]
b=[]
n=int(input("Enter: "))
for i in range(n):
    a.append(int(input('Enter input:')))
for i in range(n):
    b.append(int(input('Enter input:')))
print(a)
print(b) 
flag=0
for i in range(n):
    for j in range(n):
        if(a[i]==b[j]):
            flag=1
            break; 
if flag==1:
    print("Digit is present...") 
else:
    print("Digit is not present..")                     