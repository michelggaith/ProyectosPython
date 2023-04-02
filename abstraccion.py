class Lavadora():
    def __init__(self) -> None:
        pass
    def lavar(self, temp='Caliente'): 
        #Abstraer conciste en, utilizando una funcion publica, llamar a las funciones privadas dentro de la clase,
        # ocultando los metodos privados al usuario
        self._llenar_tanque_de_agua(temp)
        self._anadir_jabon()

    def _llenar_tanque_de_agua(self, temp):
        print(f'Llenando tanque con agua {temp}')
    def _anadir_jabon(self):
        print('anadiendo jabon')
    #Cabe aclarar que las funciones que empiezan con guion bajo son privadas en python

###PRINCIPAL###
if __name__ == '__main__':
 '''ejecutar solo el código dentro de la instrucción if cuando el intérprete de Python ejecuta directamente el programa. 
 El código dentro de la instrucción if no se ejecuta cuando el código del archivo se importa como un módulo.'''   
 lavadora = Lavadora()
 lavadora.lavar('Frio')

