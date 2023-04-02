class Personal:
    def __init__(self, antiguedad, especialidad) -> None:
        self.antiguedad = antiguedad
        self. especialidad = especialidad

    def sueldo(self):
        if(self.especialidad=='BF'):
            return 10*self.antiguedad
        else:
            return 15*self.antiguedad

class supervisor(Personal):
    def __init__(self, cargo) -> None:
        super().__init__(5, cargo)

class operador(Personal):
    def __init__(self, antiguo, cargo) -> None:
        super().__init__(antiguo, cargo)

if __name__ == '__main__':
    personal1 = Personal(10, 'Jefe de Desarrollo')
    print(f'Suedo del personal {personal1.sueldo()}')

    supervisor1 = supervisor('BF')
    print(f'Suedo del supervisor {supervisor1.sueldo()}')

    operador1 = operador(12, 'BF')
    print(f'Sueldo del operador: {operador1.sueldo()}')
