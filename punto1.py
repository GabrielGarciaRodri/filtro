import os
os.system('cls')

v1 = int (input("Ingrese el primer voltaje: "))
v2 = int (input("Ingrese el segundo voltaje: "))
v3 = int (input("Ingrese el tercer voltaje: "))
v4 = int (input("Ingrese el cuarto voltaje: "))
v5 = int (input("Ingrese el quinto voltaje: "))

promedio  = (v1+v2+v3+v4+v5)/5

if promedio > 220:
    print("ALTO VOLTAJE")
elif promedio <= 220:
    print("VOLTAJE CORRECTO")
    
else:
    print("DATOS NO VALIDOS")



