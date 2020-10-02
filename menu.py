import os

def numeros():
    pos=0
    neg=0
    cero=0
    entrada=int(input("Ingrese la cantidad de números a evaluar: "))
    for i in range(entrada):
        numero=int(input("Ingrese un número: "))
        if numero>0:
            pos=pos+1
        elif numero<0:
            neg=neg+1
        else:
            cero=cero+1
    print("Números positivos: ", pos)
    print("Numeros negativos: ", neg)
    print("Iguales a cero: ", cero)
    tecla=input("Presione una tecla para volver al menú")

def datos():
    suma=0
    edad=0
    entrada=int(input("Ingrese la cantidad de personas: "))
    for i in range(entrada):
        nombre=input("Ingrese el nombre: ")
        edad=int(input("Ingrese la edad: "))
        suma+=1
        edad+=edad
    
    print("La edad promedio es: ", edad/suma)
    tecla=input("Presione una tecla para volver al menú")
    

x=True
while(x):
    os.system('cls')
    print("1.- Números")
    print("2.- Datos personales")
    print("3.- Finalizar")
    print("")
    opc=int(input("Ingresa una opción: "))
    if(opc==1):
        numeros()
    elif(opc==2):
        datos()
    elif(opc==3):
        print("Programa finalizado")
        tecla=input("Presione una tecla")
        break
3