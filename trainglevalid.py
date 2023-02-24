a,b,c=input(print("Enter the Three angles of Triangles:")).split()
a=int(a)
b=int(b)
c=int(c)
m=min(a,b,c)
if m<0:
    print("Input angles are not of Triangles...")
else:
    sum=a+b+c
    if sum>180 :
        print("Input angles are not of Triangles...")
    else:
        print(a,b,c,"All three angles are  valid in triangle...")
