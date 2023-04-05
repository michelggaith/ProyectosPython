def lower(elementos): return elementos.lower()

lista = ['MARia', 'JUAN', 'SI']
print(list(map(lower,lista)))      #List y map son funciones propias de python

print([i.lower() for i in lista])

def saludar(idioma):
    def saludar_es():
        print('Hola')
    def saludar_en():
        print('Hi')
    func_idioma={
        'es': saludar_es,
        'en': saludar_en
    }
    return func_idioma[idioma]
el_saludo = saludar('es')
el_saludo()

from functools import reduce

numeros = (1,2,3,4)
def suma(x,y):
    return x+y
sumar = reduce(suma,numeros)  #Primero la funcion y despues los numeros
print(sumar)