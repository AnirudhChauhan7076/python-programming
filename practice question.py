'''q1

n=int(input("enter number of days"))
x=n//7
y=n%7
print('number of weeks:',x, 'number of days:',y)'''

'''q2
x=input('enter c for celcius and f for farenhite')
y=float(input("enter value"))

if x=='c':
    F=((9/5)*y)+32
    print(F)
elif x=='f':
    C=((5/9)*F)-32
    print(C)
else:
    print("enter either c or f only")'''

'''q3
b=float(input("enter value of base"))
h=float(input("enter value of height"))
area=0.5*b*h
print(area)'''

'''q4
age=int(input("enter age"))
if age>=18:
    print('You are eligible for vote')
else:
    print("You are a chotta bachha")'''

'''q5
x=int(input('enter 1st number'))
y=int(input('enter 2nd number'))
if x>y:
    print(x,'is greater')
elif y>x:
    print(y,'is greater')
else:
    print('both',x,'&',y, 'are equal')'''



'''q6
s=int(input('enter seconds'))
m=s//60
h=m//60
s=s%60

if s==60:
    
    s=s-60
elif m==60:
    
    m=m-60
print('number of hrs:',h,'number of mins:',m, 'number of secs:',s)'''


'''q7
sum=0
n=int(input('enter last number'))
for i in range(2, n+1, 2):
    sum=sum+i
    
print(sum)'''


'''q8
a=float(input("enter 1st side"))
b=float(input("enter 2nd side"))
c=float(input("enter 3rd side"))
s=(a+b+c)/2

area=(s*(s-a)*(s-b)*(s-c))**0.5
print(area)'''


'''q9
a=float(input("enter radius of sphere"))
volume=(4/3)*3.14*a**3
print(volume)'''

'''q10'''
r=float(input("enter radius of cylinder"))
h=float(input("enter height of cylinder"))
volume=3.14*h*r**2
print(volume)





