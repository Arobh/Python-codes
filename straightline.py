'''a=set()
print(type(a))
b={}
print(type(b))
'''
'''
ls={'Sunil',10,10,'35.50'}
print(ls)
nd={10,10,10,10,10}
print(nd)
'''
'''str1={'Morning','Sunil'}
print(str1)
str2={(10,20),(15,25)}
print(str2)
'''
'''
se={'Suni','Kumar','Singh','Is','a','Boring','Proffessor'}
for ele in se:
    print(ele)
    #or you can simply use print(se)
'''
'''lst=[10,20,30,40]
tpl=('Sunil',10,35.50)
set2='Set theory'
print(set(lst))
print(set(tpl))
print(set(set2))
'''
'''
dict1={'C0':'Sunil','C1':'Ravi','C3':'Shyam','C4':'Reeta'}
print(dict1) 
'''
x1,y1=input('Enter two number: ').split()
x2,y2=input('Enter 2nd: ').split()
x3,y3=input('Enter 3rd: ').split()
x1=int(x1)
x2=int(x2)
x3=int(x3)
y1=int(y1)
y2=int(y2)
y3=int(y3)
d1=((x2-x1)**2+(y2-y1)**2)**0.5
d2=((x2-x3)**2+(y2-y3)**2)**0.5
d3=((x3-x1)**2+(y3-y1)**2)**0.5
if (d1+d2==d3)or(d1+d3==d2)or(d2+d3==d1):
    print("ho rha hai")
else:
    print("nahi")    