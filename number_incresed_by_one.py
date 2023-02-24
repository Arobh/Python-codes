def increasebyone(num):
     for i in range(5):
        if num[i]==9:
            num[i]=0
        else:
            num[i]+=1    
#num=int(input('Enter the input: '))
#increasebyone(num) 
num=[]
for i in range(5):
    num.append(int(input('Enter input:')))
increasebyone(num)
print(num)
print('\n')  
for i in num:
    print(i,end='')  