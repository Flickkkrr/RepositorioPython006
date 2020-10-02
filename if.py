numero1=int(input("Ingrese un número: "))
numero2=int(input("Ingrese otro número: "))

print("Suma: ", numero1 + numero2)
print("Multiplicación: ", numero1 * numero2)
if(numero1>numero2):
    print("El ", numero1, " es mayor que el ", numero2)
elif(numero1<numero2):
    print("El ", numero2, " es mayor que el ", numero1)
else:
    print("Los números son iguales")
    