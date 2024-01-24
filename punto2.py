import os
os.system('cls')

base = float(input("Ingrese la base del triangulo: "))
altura = float(input("Ingrese la altura del triangulo: "))

rta = (base*altura)/2

if rta < 1000:
    print(f"El area del triangulo es: {rta}")
    
else:
    print("DATOS NO VÀLIDOS")