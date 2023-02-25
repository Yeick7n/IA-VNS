print("╔════════════════════════╗")
print("║   INGRESO A LA FIESTA  ║")
print("╚════════════════════════╝")


Edad=int(input("Digite su edad: "))

if(Edad>=20):
    print("Usted puede entrar a la fiesta")
elif(Edad<=20):
    print("usted no puede entrar a la fiesta")

print("╔══════════════════════════╗")
print("║  FIN INGRESO A LA FIESTA ║")
print("╚══════════════════════════╝")


print("╔══════════════════════════╗")
print("║       NUMERO MAYOR       ║")
print("╚══════════════════════════╝")


n1=int(input("digite el primer numero:"))
n2=int(input("digite el segundo numero:"))
n3=int(input("digite el tercer numero:"))

if(n1>n2 and n1>n3):
    print("n1 es el mayor: ", n1)
elif(n2>n1 and n2>n3):
    print("n2 es el mayor: ", n2)
else:
    print("n3 es el mayor: ", n3)

print("╔══════════════════════════╗")
print("║     FIN NÚMERO MAYOR     ║")
print("╚══════════════════════════╝")



print("╔══════════════════════════╗")
print("║       FUNCIÓN SUMA       ║")
print("╚══════════════════════════╝")

One=int(input("digite el primer numero:"))
two=int(input("digite el segundo numero:"))
three=int(input("digite el tercer numero:"))
four=int(input("digite el cuarto numero:"))

def suma(a,b,c,d):
    print("la suma es:", a+b+c+d)

suma(One,two,three,four)

print("╔══════════════════════════╗")
print("║     FIN FUNCIÓN SUMA     ║")
print("╚══════════════════════════╝")


print("╔══════════════════════════╗")
print("║   FUNCIÓN NUMERO MAYOR   ║")
print("╚══════════════════════════╝")

Numero1=int(input("digite el primer numero:"))
Numero2=int(input("digite el segundo numero:"))
Numero3=int(input("digite el tercer numero:"))

def mayor(a, b, c):
   if(a>b and a>c):
       print("a es mayor ", a)
   elif(b>a and b>c):
       print("b es mayor: ",b)
   else:
       print("c es mayor: ",c)

mayor(Numero1,Numero2,Numero3)

print("╔══════════════════════════╗")
print("║ FIN FUNCIÓN NUMERO MAYOR ║")
print("╚══════════════════════════╝")


print("╔══════════════════════════╗")
print("║    INGRESO DE USUARIO    ║")
print("╚══════════════════════════╝")

Nombre="Yeickon Cardozo"
Usuario="Yeick7n"
Contraseña="yeickon123"


usuario=input("Digite su usuario: ")
contraseña=input("Digite su contraseña: ")

if(usuario==Usuario and contraseña==Contraseña):
    print("Bienvenido Señor", Nombre)
else:
    print("Usuario o clave son incorrectos, intente nuevamente")


print("╔══════════════════════════╗")
print("║  FIN INGRESO DE USUARIO  ║")
print("╚══════════════════════════╝")


print("╔══════════════════════════╗")
print("║  FIN INGRESO DE USUARIO  ║")
print("╚══════════════════════════╝")


