x=10
print("el valor de x es:", x)
print("el tipo de variable es:", type(x))

m="mama"
print("el valor de mama es:", "mama")
print("el tipo de variable es:", type(m))

f=True
print("el valor de true es:", True)
print("el tipo de variable es:", type(f))

g=1
d=3
print("1+3")
print("el valor de la suma es:", g+d)

a=10
b=5
r=a+b
print("el valor de la suma es:", r)

print("el valor de la multiplicación es:", a*b)

print(10>9)
print(4<2)
print(4==3)
print(3!=2)
print(2==2)

edad=29

if edad>=18: 
    print("es mayor de edad")
else:
    print("es menor de edad")


edad=int(input("digite la edad:"))
if edad>=18: 
    print("es mayor de edad")
else:
    print("es menor de edad")

num=8
if (num%2)==0:
    print("el numero es par")
else:
    print("el numero es impar")

def suma(a,b):
    return(a+b)
print("la suma es:", suma(10,10))

def resta(a,b):
    return(a-b)
print("la resta es:", resta(10,10))

def multiplicación(a,b):
    return(a*b)
print("la multiplicación es:", multiplicación(10,10))

def división(a,b):
    return(a/b)
print("la división es:", división(10,10))

a=12
b=12
sumar=lambda a,b: a+b
print("la suma es:", sumar(a,b))

nombre="yeickon"
def saludar():
    print("hola como estas "+ nombre)
saludar()


total=500.000
mes="Febrero"

if mes=="enero":
    descuento=(total*5)/100
    neto=total-descuento
if mes=="febrero":
    descuento=(total*10)/100
    neto=total-descuento
if mes=="marzo":
    descuento=(total*15)/100
    neto=total-descuento

print("el descuento es:", descuento)
print("el neto es:", neto)