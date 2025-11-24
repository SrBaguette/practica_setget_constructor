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
    def mostrar2(self): #se ejectura un ciclo para imprimir los datos de cada persona como lista
        c=0 #contador para indicar el numero de persona
        if not len(self.listaPersonas):
            print("No hay personas inscritas.")
        else:
            for p in self.listaPersonas: #ciclo para recorrer toda la listaPersonas
                c=c+1
                print(c,". Nombre: ",p.nombre," Apellido: ",p.apellido," Identificación:",p.identificacion," Edad: ",p.edad," Correo: ",p.correo," Ocupación: ",p.ocupacion," Genero: ",p.genero)
    
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
    
    def buscar(self):
        identificacion=input("ingresa el numero de identificacion: ") #numero de identificacion de la perosna a buscar
        veri=0           
        if self.listaPersonas:#verifica que la lista no este vacioa 
            for p in self.listaPersonas :#recorre la lista
                if p.identificacion == identificacion :#busca que el numero de identificacion se ale mismo que estamos Buscando
                    veri=1
                    p.mostrardatos()#muestra la persona
            if veri==0:
                print("no se encontro la persona")    
        else:
            print("la lista esta vacia")
   
    def cambiar(self):
        identificacion=input("ingresa el numero de identificacion: ") 
        veri=0          
        if self.listaPersonas:#verifica que la lista no este vacia
            for p in self.listaPersonas :#recorre la lista
                if p.identificacion == identificacion :
                    veri=1
                    #se  piden los nuevos varores
                    nombre=input("Ingrese el nombre: ")
                    apellido=input("Ingrese el apellido: ")
                    identificacion=input("Ingrese el numero de indetificación: ")
                    identificacion=self.checka(identificacion) #revisa si el numero esta repetido y si es un numero
                    edad=input("Ingrese la edad: ")
                    edad=self.esnum(edad) #Revisa si la edad es un numero
                    correo=input("Ingrese el correo: ")
                    ocupacion=input("Ingrese la ocupación: ")
                    genero=input("Ingrese el genero: ") #aca se le piden los datos al cliente
                    #-----se agregan los nuevos valores----- 
                    p.nombre=nombre
                    p.apellido=apellido
                    p.identificacion=identificacion
                    p.edad=edad
                    p.correo=correo
                    p.ocupacion=ocupacion
                    p.genero=genero
                    print("\ncambio de datos")
                    p.mostrardatos()#muestra a la persona
            if veri==0:
                print("no se encontro la persona")    
        else:
            print("la lista esta vacia")
    