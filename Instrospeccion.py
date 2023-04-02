class intro:
    def __init__(self, valor) -> None:
        self.valor = valor
    def segundo(self):
        print('segundo')
    def tercero(self):
        print('Tercero')

dato = intro('Valor')
'''
datoFinal = dir(dato)
#print(dir(dato))
for i in datoFinal:
    print(i)
    '''
print(isinstance(dato, intro))  #Devuelve un true o false preguntando si el objeto es una instancia de la clase intro
print(hasattr(dato, intro))     #Busca variables DE CLASE y devuelve True o Flase si en la clase hay una