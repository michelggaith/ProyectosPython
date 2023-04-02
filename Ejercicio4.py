def indice(ind):
    lista = [1,2,3,4,5,6,7,8,9,10]
    try:
        print(lista[ind])
    except IndexError:
        print(f'Error en el indice {ind}')
    else:
        print('No hay error')

indice(1)

