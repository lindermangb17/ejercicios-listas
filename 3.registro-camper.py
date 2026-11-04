

codigo=input("Ingrese su codigo: ")

nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
nombrecomp=nombre+" "+apellido


print("Ingrese su fecha de nacimiento")

dia=input("Ingrese su día de nacimiento: ")
mes=input("Ingrese su mes de nacimiento: ")
año=input("Ingrese su año de nacimiento: ")

fecha=(dia,mes,año)

camper=(codigo,nombre,apellido,fecha)

print(f"nombre completo: {camper[1]} {camper[2]} ")
print(f"Año de nacimiento: {fecha[2]}")
print(f"elementos tupla: {len(camper)}")
print(f"cuarto elemento: {camper[3]}")
