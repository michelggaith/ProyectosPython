class Lavadora():
    def __init__(self) -> None:
        pass
    def lavar(self, temp='Caliente'): 
        self._llenar_tanque_de_agua(temp)
        self._anadir_jabon()
        self._lavar()
        self._Centrifugar()

    def _llenar_tanque_de_agua(self, temp):
        print(f'Llenando tanque con agua {temp}')
    def _anadir_jabon(self):
        print('anadiendo jabon')
    def _lavar(self):
        print('Se esta lavando')
    def _Centrifugar(self):
        print('Se esta centrifugando')

if __name__ == '__main__':
 lavadora = Lavadora()
 lavadora.lavar('Fria')

