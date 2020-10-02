par=0
impar=0
for i in range (1, 11):
    
    a1=int(input(("Ingrese un número: ")))
    if a1%2==0:
        print("Es par")
        
        par=par+1
    else:
        print("Es impar")
        
        impar=impar+1
print("Hay ", par, " número(s) par(es)")