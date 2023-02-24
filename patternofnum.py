def pattern(n):
    num=1
    for i in range(0,n):
        for j in range(0,n-i):
            print(' ',end=' ')
        for k  in range(0,i):
            print(num," ",end=' ')
            num+=1
        print('\n')    
n=int(input("Enter the number of rows..."))
pattern(n)            