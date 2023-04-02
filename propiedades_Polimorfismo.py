'''
class Circulo:
    
    def __init__(self, radio) -> None:
        self.radio = radio
    
    @property           #Tal como su nombre dice, define una propiedad, no la paso como parametro pero es funcion del resto de parametros definidos
    def area(self):     #al momento de crear el objeto
        return 1.004545*(self.radio**2)
    

c= Circulo(10)
print(c.area)
'''
#Polimorfismo
class Perro:
    def avanzar(self):
        print("Tengo 4 patas")
class Perico:
    def avanzar(self):
        print("Volar")

def mover(animal):      #Al definir con polimorfismo podemos establecer una funcion global, al llamar a la funcion mover (animal), llama
    animal.avanzar()    # A la funcion correspondiente de la clase con el mismo nombre!

perro= Perro()
perro.avanzar()
perico = Perico()
perico.avanzar()

mover(perro)
mover(perico)


        
