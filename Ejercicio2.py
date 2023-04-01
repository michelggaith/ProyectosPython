class Persona():
    def __init__(self, nombre, edad, nacionalidad, DNI):
        self.nombre=nombre
        self.edad = edad
        self.nacionalidad=nacionalidad
        self.DNI = DNI
    def NombreyEdad(self):
        print(f'El nombre es {self.nombre}')
    def devuelve_edad(self):
         print(f'La edad {self.edad}')
    @classmethod
    def devuelve_DNI(cls, DNI, nacionalidad):
        print(f'Su DNI es {DNI}  y nacionalidad es {nacionalidad}')
    def __str__(self):
        return f'{self.nombre} edad {self.edad} DNI {self.DNI} nacionalidad {self.nacionalidad}'

persona1 = Persona('Michel', 25, 'Argentina', 40963813)
persona1.NombreyEdad()
persona1.devuelve_edad()
persona1.devuelve_DNI(40963813, 'Argentina')
print(persona1)