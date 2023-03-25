'''
#Ejercicio 1
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

r = ((c+5)*(b**2-3*a*c)*a**2)/(4*a)
print(f"La respuesta es: {r}")

#Ejercicio 2

a = float(input("a: "))
b = float(input("b: "))
print(f"El nuevo valor es:{a} y {b}")
a,b = b,a
print(f"El nuevo valor es:{a} y {b}")

#Ejercicio 3

r = float(input("Ingrese el radio: "))
area = math.pi*r**2
longitud = 2*math.pi*r
print(f"Area = {area:.1f} y longitud = {longitud:.1f}")
'''
#Ejercicio 4
import math
precio = float(input("Ingrese el precio: "))
descuento = precio*0.36
precioFinal = precio-descuento
print(f"Precio Inicial = {precio},el descuento es {descuento}, aplicando descuento = {precioFinal}")