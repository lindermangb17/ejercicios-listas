cant=int(input("Cantidad de temperaturas: "))

temperaturas=[]
suma=0

for t in range(1,cant+1):
    temp=float(input(f"temperatura #{t}: "))
    temperaturas.append(temp)
    suma=suma+temp

media= suma/cant

superior=[]

for x in temperaturas:
    if x >= media:
        superior.append(x)

print(f"Temperatura media: {media}")
print(f"Temperaturas >= media: {superior}")
print(f"Total: {len(superior)}")




