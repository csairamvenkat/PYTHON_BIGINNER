#assingment operator
x=2
x=x+2
print(x)
x-=2         #output:0
print(x)
x/=2
print(x)      #o:1.0
x*=6
print(x)      #o:6.0
x//=2
print(x)      #o:3.0

#unary operator
m=7
n=-(m)
print(n)         #o:-7

#relational operators
a=5
b=6
print(a<b)
print(a>b)
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)

#logical operator
a=5
b=7
print(a<8 and b<9)
print(a<8 and b>9)
print(a<8 or b>9)
print(a<8 or b<9)
print(a>9 or b>9)
c=False
print(not c)