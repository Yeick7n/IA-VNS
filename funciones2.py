def menu():
    print("╔═════════════════════════╗")
    print("║    MENÚ PRINCIPAL       ║")
    print("║    1.Suma               ║")
    print("║    2.Resta              ║")
    print("║    3.Multiplicar        ║")
    print("║    4.División           ║")
    print("║    5.Modulo             ║")
    print("║    6.Potencia           ║")
    print("║    7.Salir              ║")
    print("╚═════════════════════════╝")

def vocal(letra):
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
      print("La letra es una vocal")
    else:
        print("Es una consonante")