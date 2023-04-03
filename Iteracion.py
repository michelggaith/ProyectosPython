for i in open('README.md'):
    print(i)

#GENERADORES Obtenemos informacion "Gota a Gota"

def generaPares(limite):
    num = 1
    miLista = []
    while num < limite:
        '''miLista.append(num*2)
        num = num+1
    return miLista'''
        yield num*2             #Es lo mismo que un return pero respeta la iteracion del bucle y lo pausa hasta que se lo llama
        num = num+1
"""
En vez de generar  toda una lista directamente (como en la otra parte comentada, 
lo hace una vez por vez, gota a gota hasta que volvamos a llamar)
"""
devuelvepares = generaPares(10)
#print(generaPares(10))
print(next(devuelvepares))
print(next(devuelvepares))
print(next(devuelvepares))
print(next(devuelvepares))
print(next(devuelvepares))