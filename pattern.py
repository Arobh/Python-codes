n=int(input(print("Enter the number of rows:")))
a=1
b=1
for i in range(1,n+1):
    print(end=" "*(n+1-b) )
    for j in range(1,i+1):
        print(a,end=" ")
        a=a+1
    b=b+1
    print()    
    