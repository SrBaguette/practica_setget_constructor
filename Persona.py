from typing import List
class Persona: #clase persona para almacenar datos de la persona
    def __init__(self,nombre,edad,identificacion):
        self.nombre=nombre
        #self.apellido=apellido
        self.edad=edad
        #elf.correo=correo
        #self.ocupacion=ocupacion
        #elf.genero=genero
        self.identificacion=identificacion
    def mostrardatos(self): #mostrar los datos guardados en el constructor
        print("Nombre: ",self.nombre," Apellido: "," Identificación:",self.identificacion," Edad: ",self.edad," Correo: "," Ocupación: "," Genero: ")

        #print("Nombre: ",self.nombre,"\n Apellido: ","\n Identificación:",self.identificacion,"\n Edad: ",self.edad,"\n Correo: ","\n Ocupación: ","\n Genero: ")

#recuerda anadir los faltantes
