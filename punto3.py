import os
os.system('cls')

v1 = int (input("Ingrese el primer voltaje: "))
v2 = int (input("Ingrese el segundo voltaje: "))
v3 = int (input("Ingrese el tercer voltaje: "))

promedio = (v1+v2+v3)/3

if promedio <= 115:
    print("VOLTAJE CORRECTO")
elif promedio > 115 and promedio < 220:
    print("ALTO VOLTAJE")
elif promedio >= 220:
    print("PELIGRO")
    
else:
    print("LA OPCION NO ES VALIDA. . .")