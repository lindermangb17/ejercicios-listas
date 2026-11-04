num=int(input("Cantidad: "))
numeros=[]

for x in range(1,num+1):
    numero=int(input(f"numero #{x}: "))
    numeros.append(numero)

buscar=int(input("Número a buscar: "))


for i in range(len(numeros)):
    if numeros[i] == buscar:
        print(f"El {buscar} esta en la posicion {i}")
        break
else:
    print(f"El {buscar} no esta en la lista")

