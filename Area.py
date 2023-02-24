R_l =float(input(print("Enter the length of Rectangle : ")))
R_b =float(input(print("Enter the breadth of Rectangle : ")))
if R_l>=0 and R_b>=0 :
    print("Area of rectangle = ",R_l*R_b)
    print("Perimeter of rectangle = ",2*(R_l+R_b))
else:
    print("invalid input for rectangle")    
C_r =float(input(print("Enter the radius of circle : ")))
if C_r>=0:
    print("Area of circle = ",3.14*C_r**2)
    print("Perimeter of rectangle = ",2*3.14*C_r)
else :
    print("Invalid input for Circle")