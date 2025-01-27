# # # int ,float,string,boolean,complex-->Primitive Data Type
# # #Non Primitive-->Built In-->List,Tuple,Dictionary,Set
# # #Non Primitive-->USer Defined-->Stack,Linked List,Queue
# # import math
# # # i=100 #int
# # # a=10.8 #float
# # # x="sai" #string
# # # y=True #boolean
# # # W=None
# # # #print(W)
# # # # #print(i,a,x,y)
# # # # #print(type(i) , type(a), type(x). type(y))
# # # f1=3e0
# # # # #print(f1)
# # # f2=3e1
# # # # #print(f2)
# # # f3=3e2  #e1 means 10 power 1
# # # # #print(f3)
# # # f4=2.3e4 
# # # #print(f4)
# # # # Example: Calculate 2 to the power of 3
# # # result = 2 ** 3
# # # #print(result)  # Output: 8

# # # # Example: Calculate 2 to the power of 3
# # # result = pow(2, 3)
# # # #print(result)  # Output: 8

# # # # Example with modulus: Calculate (2^3) % 5
# # # result_mod = pow(2, 3, 5)
# # # #print(result_mod)  # Output: 3

# # # #print(True+False) # True=1, False=0-->BODMAS rule is used for calculation

# # a=100
# # b=30
# # c=a+b
# # ##print("Sum of",a,"and",b ,"is", c)

# # # Complex Data Type
# # #complex=a+bj a is real , b is imaginary and j is sqrt(-1)
# # a=30
# # b=10+30j
# # c=10+20j
# # #print(type(c))
# # #print(a+b+c)
# # #print(b*c) #100+200j+300J-600
# # #print(b.real)
# # #print(b.imag)
# # # j=19
# # # #print(j)

# # #STRING
# # s='naresh'
# # #print(s)
# # #print(type(s))
# # s2='''nareshit
# # technology'''
# # #print(s2)
# # #STRING SLICING (:)
# # #print(s[0:4])   #0 to n-1
# # #print(s[1:-4])
# # #print(s[2:-1])
# # #print(s[0:7:2])   #here 2 is step index
# # #STRING CONCATANATION
# # s6='hello'
# # s7='hi'
# # s8=s6+s7
# # #print(s8)           #output:hellohi

# # # 1-Arithmetic
# # a=5
# # b=6
# # c=a+b
# # #print(c)

# # d=int.__add__(5,6)
# # e=int.__sub__(5,6)
# # #print(d)
# # #print(e)
# # f=int.__mul__(5,6)
# # g=int.__divmod__(7,2)
# # #print(f)
# # #print(g)

# # x=10
# # y=5
# # z=x//y      #output:quotient
# # #print(z)
# # z1=x%y      #output:reminder
# # #print(z1)

# # my_string = "Hello, World!"

# # # Accessing the last character
# # #print(my_string[-1])  # Output: '!'

# # # Accessing the second-to-last character
# # #print(my_string[-2])  # Output: 'd'

# # # Accessing the third-to-last character
# # #print(my_string[-3])  # Output: 'l'

# my_string = "SaiRamVenkat"
# #print(my_string[-5:])  # Output: 'enkat'  last n charcters are considered

# import math

# # Square root
# # #print(math.sqrt(16))  # Output: 4.0

# # Trigonometric functions
# # #print(math.pi / 2)
# # #print(math.sin(math.pi / 2))  # Output: 1.0

# # Logarithms
# # #print(math.log(10))  # Natural log (base e)

# # Factorial
# # #print(math.factorial(5))  # Output: 120

# #Type Casting of int,float take only 1 arg 
# #Type Casting of complex take  max 2 arg 

# #print(int(2.4))
# #print(int(True))
# ##print(int(1+2j)) #error type casting complex to int
# ##print(int('10.9')) errpr
# #print(float('10.9')) #10
# ##print(int(10.3,20.5)) #error
# ##print(float(10.3,20.8)) #error 
# #print(complex(1)) #1+0j
# #print(complex(2,1)) #2+1j
# ##print(complex(2,1,3)) #error
# #print(complex(18.2,8))
# #print(complex(True,False))
# #print(complex(False))
# #print(complex(False,True))
# ##print(complex('True','False'))  #error cannot take 2nd arg if 1st arg is string
# import cmath
# #print(cmath.sqrt(-4))

# print(str(10))  #'10'
# print(str(10.19)) #'10.19'


# print(bool())
# print(bool( ))
# print(bool(10))
# print(bool(10+2j))
# print(str(10+9j))


# # .ipynb (interactive python note book) and .py are file extensions
print(type(str(10.19))) #'10.19'