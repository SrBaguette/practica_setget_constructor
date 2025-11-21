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

class AdministrarDatos: #clase creada para administrar datos
    def __init__(self):
        self.listaPersonas:List[Persona]=[] #se crea una lista nueva para almacenar los objetos de tipo Persona
    def addper(self,persona: Persona): #se usa un append para añadir los objetos a la lista
        self.listaPersonas.append(persona)
    def mostrar(self): #se ejectura un ciclo para imprimir los datos de cada persona
        c=0 #contador para indicar el numero de persona
        for lista in self.listaPersonas: #ciclo para recorrer toda la listaPersonas
            c=+1
            print("Persona #",c)
            lista.mostrardatos() #se cita el objeto y se ejecuta la función mostrardatos de la anterior clase
    def borrar(self,numero): #en base al numero de la persona se borra el elemento de la lista.
        del self.listaPersonas[numero-1] #del borra el elemento de la posicion indicada
        print("Persona Borrada")

