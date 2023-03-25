#Condicional if
'''
dato = int(input("Ingrese un numero: "))
if (dato>0): 
    print("Numero Positivo")
    print("Segundo positivo")
elif dato==0:
    print("Resultado igual a 0")
else:
    print("Dato negativo")

#Ejercicio 1 IF

n1 = int(input("ingrese el primer numero"))
n2 = int(input("Ingrese el segundo numero"))

if (n1%2 == 0 and n2%2 == 0):
    print("Ambos son pares")
elif (n1%2==0 and n2%2 !=0):
    print(f"El numero {n2} es impar")
    
elif (n1%2!=0 and n2%2 ==0):
    print(f"El numero {n1} es impar") 
else:
    print("Ambos son impares")

print("Fin del programa")

#Ejercicio 2 IF

n1 = int(input("ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
n3 = int(input("Ingrese el tercer numero: "))

if(n1>=n2 and n1>=n3):
    print(f"{n1} es mayor")
elif(n2>=n1 and n2>=n3):
    print(f"{n2} es mayor")
else: 
    print(f"{n3} es mayor")

#Ejercicio 3 IF

nombre1 = input("Ingrese el primer nombre: ")
nombre2 = input("Ingrese el segundo nombre: ")

if(nombre1[0]==nombre2[0] and nombre2[-1]==nombre1[-1]):
    print("Hay coincidencia")
else:
    print("No hay coincidencia")
'''
#Ejercicio 4 IF (CAJERO)

Saldo = 2000
print("Menu de inicio: ")
print("1. Ingresar Dinero")
print("2. Retirar dinero")
print("3. Mostrar Dinero")
print("4.Salir")

seleccion = int(input("Elija una opción: "))

if(seleccion==1):
    ingreso = float(input("Ingrese la cantidad deseada: "))
    Saldo +=ingreso
    print(f"Nuevo saldo = {Saldo}")
elif(seleccion==2):
    salida = float(input("Ingrese la cantidad deseada: "))
    if(salida>Saldo):
        print("Saldo Insuficiente")
    else:
         Saldo -=salida
    print(f"Nuevo saldo = {Saldo}")
elif(seleccion==3):
    print(f"Saldo = {Saldo}")
elif(seleccion==4):
    print("Salida")
else:
    print("Ingreso erroneo")
