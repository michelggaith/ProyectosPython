#Introduccion a los arrays
array = ["futbol", "PC", 18.6, 18, [6,7,10.4], True, False]
#Imprimir ultimo valor de la lista
print(array[-1])
#Imprimir longitud de la lista
print(len(array))
#Imprimir apartir de
print(array[2:]) 
#Añadir al final de la lista
array.append(66)
print(array)
#Añadir al array en la posicion 2 el elemento indicado
array.insert(2, True)
print(array)
#Añado elementos al final de la lista
array.extend([True,19.5, 6])
print(array)
array2 = [1,5, 255, 12.8]
#Concatenar arreglos
array3 = array+array2
print(array3)
#Buscar Palabras
print("PC" in array)
 #ENCUENTRA EL INDICE DONDE ESTA
print(array.index("PC"))
# Cuenta la cantidad de veces que la palabra se repite 
print(array.count("PC")) 
#ELIMINA LO INDICADO
array.remove("PC") 
print(array)
#INVIERTE LA POSICION DE LOS ELEMENTOS
array.reverse()
print(array)
#ORDENA DE MENOR A MAYOR LOS ELEMENTOS

array2.sort()
print(array2)
#ORDENA DE MAYOR A MENOR LOS ELEMENTOS
array2.sort(reverse=True)
print(array2)
#LIMPIA COMPLETAMENTE LA LISTA
array.clear()
print(array)

