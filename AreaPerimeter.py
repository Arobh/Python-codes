len=float(input(print("Enter the length of rectangle: ")))
bre=float(input(print("Enter the breadth of rectangle: ")))
if min(len,bre)<0:
    print("Length and Breadth parameter of rectangle is  invalid")
else:
    area=len*bre
    peri=2*(len+bre)
    if(area>peri):
        print(area,"Area is greater than Perimeter of Rectangle...",peri)
    elif(area==peri):
        print(area,"Area is equal to the Perimeter of Rectangle...",peri)
    else:
        print(area,"Area is lesser than Perimeter of Rectangle...",peri)