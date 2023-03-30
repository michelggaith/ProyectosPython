class Libro():
    def __init__(self, nombre, autor, paginas) -> None:
        self.nombre = nombre
        self.autor = autor
        self.paginas = paginas
    
    def describir(self):                             #La diferencia de este metodo con los otros es que al mismo HAY que instanciarlo, a los otros no
        print(f'Hola desde describir {self.nombre}')
    
    def __str__(self) -> str:                       #Este metodo es especial, lo busca sin necesidad de instanciar
        return f'{self.nombre} escrito por {self.autor}'
    
    def __len__ (self):         #Basicamente si quiero usar LEN con el objeto sin necesidad de instanciar, puedo añadir esto
        return self.paginas     #lo cual me permite utilizar la funcion len en el objeto, tal como el print con el objeto
    def __del__ (self):         #Permite, sin errores, eliminar el objeto
        print('Se ha eliminado un objeto')

    

libro1 = Libro('Curso Python', 'Brian', 110)
print(libro1)
del libro1
