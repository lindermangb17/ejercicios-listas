numeros=[]
pares=[]
impares=[]

num = 0


while num !=99999:
    num=int(input("Ingrese un numero: "))

    if num!=99999:
        numeros.append(num)

for i in numeros:
    if i%2==0:
        pares.append(i)
    else:
        impares.append(i)


print(f"Pares: {pares} (total {len(pares)})")    
print(f"Impares: {impares} (total {len(impares)})")   