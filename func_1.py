from math import pi
def f(x):
    y = 2 * x ** 2 + 1
    return y

b = 4
c = 7
def areatriangulo(a,b,c):
    perimetro = a + b + c  
    return perimetro

def cuadrado(l):
    area = l ** 2
    return area

def rectangulo(a,b):
    area = a * b
    return area

def circulo(h):
    area = pi * h ** 2
    return area

for x in range(5):
    y = f(x)
    print (x,y)
print ""
for x in range (5):
    y = areatriangulo(x,b,c)
    print(x,y)
print ""
for x in range (4):
    y = cuadrado(x)
    print (x,y)
print ""
for x in range (5):
    y = rectangulo(x,b)
    print (x,y)
print ""
for x in range (5):
    y = circulo(x)
    print (x,y)
print ""
def dif(num1,num2):
    if (num1>num2):
        aux = num1
        num1 = num2
        num2 = aux
    for i in range(num1+1,num2):
        print(i)
dif(43,54)