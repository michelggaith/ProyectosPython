#While
'''
numero = 0
while numero<20:
    numero+=1
    if(numero==10):
        print(numero+4)
    print(numero)

import math
numero=int(input("Ingrese un numero"))
while numero<0:
    print("Ingrese un numero positivo")
    numero=int(input("Ingrese un numero"))
print(f"La raiz cuadrada es: {math.sqrt(numero):.2f}")

#For
data = [6,8,9,4,7]
for i in data:
    print(f"Objeto: {i}")
'''
#Ejercicio for sumatoria del 0 al 100:
total = 0
for i in range(0,11,2):
    total+=i
print(total)
#Cambio URgente