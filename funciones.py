from typing import List
class Persona:
    def __init__(self,nombre,apellido,edad,correo,ocupacion,genero,identificacion):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.correo=correo
        self.ocupacion=ocupacion
        self.genero=genero
        self.identificacion=identificacion
    def mostrardatos(self):
        print("Nombre: ",self.nombre,"\n Apellido: ",self.apellido,"\n Identificación:",self.identificacion,"\n Edad: ",self.edad,"\n Correo: ",self.correo,"\n Ocupación: ",self.ocupacion,"\n Genero: ",self.genero)

class AdministrarDatos:
    def __init__(self):
        self.listaPersonas:List[Persona]=[]
    def addper(self,persona: Persona):
        self.listaPersonas.append(persona)
    def mostrar(self):
        return [p.mostrardatos() for p in self.listaPersonas]
    def borrar(self,numero):
        del self.listaPersonas[numero-1]
        print("Persona Borrada")

