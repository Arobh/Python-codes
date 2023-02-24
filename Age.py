'''
ram=int(input(print("enter the age of ram ")))
shyam=int(input(print("enter the age of Shyam ")))
ajay=int(input(print("enter the age of Ajay ")))
if ram<shyam :
    if ram<ajay:
        print(ram,"ram is the youngest")
    else:
        print(ajay,"ajay is the youngest")    
else:
    if shyam<ajay:
        print(shyam,"Shyam is the youngest...")
    else:
        print(ajay,"Ajay is the youngest")
'''
ram=int(input(print("enter the age of ram ")))
shyam=int(input(print("enter the age of Shyam ")))
ajay=int(input(print("enter the age of Ajay ")))
a=min(ram,shyam,ajay)
if a==ram:
    print("Ram is the youngest...",a)
if a==shyam:
    print("shaym is the youngest...",a)
if a==ajay:
    print("Ajay is the youngest...",a)        