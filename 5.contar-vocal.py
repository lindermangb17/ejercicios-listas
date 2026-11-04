numletras=int(input("¿Cuántas letras?: "))

listaletras=[]

for x in range(1,numletras+1):
    letra=input(f"letra #{x}: ")
    if letra.isalpha():
        listaletras.append(letra.lower())

      

vocales=("a","e","i","o","u")

for vocal in vocales:
    print(f"Cantida de {vocal} = {listaletras.count(vocal)}")