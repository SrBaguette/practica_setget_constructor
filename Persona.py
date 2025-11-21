from typing import List
class Persona: #clase persona para almacenar datos de la persona
    def __init__(self,nombre,apellido,edad,correo,ocupacion,genero,identificacion):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.correo=correo
        self.ocupacion=ocupacion
        self.genero=genero
        self.identificacion=identificacion
    def mostrardatos(self): #mostrar los datos guardados en el constructor
        print("Nombre: ",self.nombre,"\n Apellido: ",self.apellido,"\n Identificación:",self.identificacion,"\n Edad: ",self.edad,"\n Correo: ",self.correo,"\n Ocupación: ",self.ocupacion,"\n Genero: ",self.genero)
