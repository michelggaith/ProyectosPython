class alumno:
    def __init__(self, nombre, edad, carrera, nota):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.nota = nota
    def aprobado(self):
        if self.nota >5:
            return True
        else:
            return False

#Inicio

alumno1 = alumno("Juan", 21, "Ingeniero", 3)
print(alumno1.aprobado())
##Control de versiones y cambios
#Cambio 
#Cambio de comentario 
#Otro cambio
#Cambio en Rama2
