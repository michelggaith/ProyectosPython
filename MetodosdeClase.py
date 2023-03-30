class Persona():
    def __init__(self): #Constructor
        pass
    def despedir(self):
        print('Te despido....')
    @classmethod  #Este es un decorador: permite llamar a una clase sin haberla inicializado ni creado su objeto
    def Saludar(cls, nombre):
        print('Te saludo desde mi metodo de clase, mi nombre es', nombre)

#############################################
persona1 = Persona()
persona1.despedir()
persona1.Saludar('Martin')
Persona.Saludar('Brian')
