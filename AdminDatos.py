from Persona import Persona
from typing import List
class AdministrarDatos: #clase creada para administrar datos
    def __init__(self):
        self.listaPersonas:List[Persona]=[] #se crea una lista nueva para almacenar los objetos de tipo Persona
    def addper(self,persona: Persona): #se usa un append para añadir los objetos a la lista
        self.listaPersonas.append(persona)
    def mostrar(self): #se ejectura un ciclo para imprimir los datos de cada persona
        c=0 #contador para indicar el numero de persona
        if not len(self.listaPersonas):
            print("No hay personas inscritas.")
        else:
            for lista in self.listaPersonas: #ciclo para recorrer toda la listaPersonas
                c=c+1
                print("Persona #",c)
                lista.mostrardatos() #se cita el objeto y se ejecuta la función mostrardatos de la anterior clase
    def borrar(self,numero): #en base al numero de la persona se borra el elemento de la lista.
        del self.listaPersonas[numero-1] #del borra el elemento de la posicion indicada
        print("Persona Borrada")
    def checka(self,checka): #funcion para revisar si hay alguna identificacion repetida y si el dato ingresado es numero
        while checka.isdigit()==False:# revisa si el texto ingresado es numero o no
            checka=input("La idenfiticación no es un numero, vuelva a ingresar: ")
            while any(p.identificacion == checka for p in self.listaPersonas): #se revisa en todos los objetos de listaPersonas si identificacion es igual al check
                checka=input("La identificación ya existe, ingrese otra: ")
        return checka
    def esnum(self,checka):
        while checka.isdigit()==False:# revisa si el texto ingresado es numero o no
            checka=input("La edad no es un numero, vuelva a ingresar: ")
        return checka