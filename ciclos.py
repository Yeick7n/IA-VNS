palabra="Real madrid"
cont=0
for I in palabra:
    cont+=1
print("la palabra tiene",cont, "letras")

sum=0
n=4
for I in range(0,n):
    sum+=I
print(sum)

suma=0
for I in range(0,3):
    suma+=I
print(suma)

edad=int(input("digite su edad: "))

if(edad<5):
    print("Va para primaria")
elif(edad>=5 and edad<10):
    print("Va para tercero de primaria")
elif(edad>=10 and edad<13):
    print("Va para quinto de primaria")
else:
    print("Va para septimo")


peso=float(input("digite su peso: "))
altura=float(input("digite su altura: "))

def calculoIMC(peso,altura):
    imc=peso / (altura*altura)
    return imc


def mostrar():
    imc=round(calculoIMC(peso,altura),3)
    print("Su IMC es: ", imc)
    if (imc <18.5):
        print("Bajo de peso")
    elif (imc >=18.5 and imc<25):
        print("Peso normal")
    elif(imc>=25 and imc<30):
        print("sobrepeso")
    elif(imc>=30 and imc<35):
        print("Obesidad tipo 1")
    elif(imc>=35 and imc<40):
        print("Obesidad tipo 2")
    elif(imc>=40 and imc<50):
        print("Obesidad tipo 3")
    else:
        print("error")

mostrar()

letra=input("digite una letra: ")

