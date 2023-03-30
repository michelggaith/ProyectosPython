class Persona():
    edad = 20
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
    def correr(self):
        print('Estoy corriendo')

##########################################
persona1 = Persona('Martin' , 'Argentina')
print(persona1.nombre)
persona1.correr()