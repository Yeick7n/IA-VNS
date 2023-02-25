

def menu():
    print("╔═════════════════════════╗")
    print("║    MENÚ PRINCIPAL       ║")
    print("║    1.Suma               ║")
    print("║    2.Resta              ║")
    print("║    3.Multiplicar        ║")
    print("║    4.División           ║")
    print("║    5.Modo               ║")
    print("║    6.Potencia           ║")
    print("║    7.Salir              ║")
    print("╚═════════════════════════╝")


menu()

op = int(input("digite el numero de la operación"))

if (op == 1):
    a = int(input("digite un número:"))
    b = int(input("digite oro número:"))

    def sumar(a, b): return a+b
    print("la suma da:", sumar(a, b))

elif (op == 2):
    a = int(input("digite un número:"))
    b = int(input("digite oro número:"))

    def restar(a, b): return a-b
    print("la resta da:", restar(a, b))

elif (op == 3):
    a = int(input("digite un número:"))
    b = int(input("digite oro número:"))

    def multiplicar(a, b): return a*b
    print("la multiplicación da:", multiplicar(a, b))

elif (op == 4):
    a = int(input("digite un número:"))
    b = int(input("digite oro número:"))

    def dividir(a, b): return a/b
    print("la división da:", dividir(a, b))

elif (op == 5):

    print("Salió del menú")
    breakpoint()

op = input("¿quiere realizar otra operación?")

op == "si"


op = int(input("digite el numero de la operación"))

if (op == 1):
    a = int(input("digite un número:"))
    b = int(input("digite oro número:"))

    def sumar(a, b): return a+b
    print("la suma da:", sumar(a, b))

elif (op == 2):
    a = int(input("digite un número:"))
    b = int(input("digite oro número:"))

    def restar(a, b): return a-b
    print("la resta da:", restar(a, b))

elif (op == 3):
    a = int(input("digite un número:"))
    b = int(input("digite oro número:"))

    def multiplicar(a, b): return a*b
    print("la multiplicación da:", multiplicar(a, b))

elif (op == 4):
    a = int(input("digite un número:"))
    b = int(input("digite oro número:"))

    def dividir(a, b): return a/b
    print("la división da:", dividir(a, b))

elif (op == 5):

    print("Salió del menú")
    breakpoint()
