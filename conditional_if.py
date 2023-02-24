a,b=input('Enter two numbers: ').split()
a=int(a)
b=int(b)
if a>=b:
    if a>b:
        print(a,'is the greatest...')
    else:
        print('both are equal...')    
else:
    print(b,'is the greatest')    