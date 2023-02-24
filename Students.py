a, b, c, d, e = input("Enter The marks of 5 students : ").split()
a=float(a)
b=float(b)
c=float(c)
d=float(d)
e=float(e)
res=max(a,b,c,d,e)
res2=min(a,b,c,d,e)
if res<=100 and res2>=0:
    ag_marks=a+b+c+d+e
    per=str(ag_marks/5)
    print("Aggregate marks=",ag_marks)
    print("percentage= ",per+" %")
else:
    print("Invalid Input")    
    