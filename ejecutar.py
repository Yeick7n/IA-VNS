from funciones2 import*
from funciones import*
while True:
    menu()
    op=int(input("digite una opción: "))
    if op==1:
         a = int(input("digite un número:"))
         b = int(input("digite oro número:"))

         print("la suma da: ",suma(a,b))
    elif op==2:
         a = int(input("digite un número:"))
         b = int(input("digite oro número:"))

         print("la resta da: ",restar(a,b))
    elif op==3:
         a = int(input("digite un número:"))
         b = int(input("digite oro número:"))

         print("la multiplicación da: ",multiplicar(a,b))
    elif op==4:
         a = int(input("digite un número:"))
         b = int(input("digite oro número:"))

         print("la división da: ",dividir(a,b))
    elif op==5:
         a = int(input("digite un número:"))
         b = int(input("digite oro número:"))

         print("El modulo da: ",modulo(a,b))
    elif op==6:
         a = int(input("digite un número:"))
         b = int(input("digite oro número:"))

         print("la potencia da: ",potencia(a,b))
    elif op==7:
        break
    else:
         print("ERROR, DIGITE DE NUEVO")