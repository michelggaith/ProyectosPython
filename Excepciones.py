'''
lista = [1,2,3]

#print(lista[4]) -> Esto me genera un error. El uso de excepciones evita que el programa se cancele o arruine todo.
try:
    print(lista[1])
except IndexError:
    print('Error en el indice')
else:
    print('No hay ningun error')
finally:
    print('se ejecuto el script correctamente')
#Ayuda en el termino de seguridad tambien.
try:
    raise TypeError         #Arroja el tipo de error la palabra Raise
except:
    print('Error con los tipos de datos..', TypeError)
'''
#Excepciones personalizadas, creo un tipo de error.
class error(Exception):
    def __init__(self, valor) -> None:
        print(f'se causo un error por: {valor}')

try:
    raise error(2)
except error:
    print('Error escrito')
