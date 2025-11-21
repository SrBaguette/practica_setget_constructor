from Persona import Persona #importación de clase Persona
from AdminDatos import AdministrarDatos #importación de clase Administrar datos
opc=-1
proce=AdministrarDatos() #Creacion de objeto proce para manejar definiciones de admindatos
while opc !=0: #ciclo para el menú
    print("Bienvenido al menú") 
    print("1. Agregar Persona \n 2. Modificar Persona \n 3. Eliminar Persona \n 4. Mostrar todas las personas \n 5. Buscar persona \n 0. Salir")
    opc=input("Ingrese una opción: ") #Imprime menú y le pide al cliente que ingrese una opción del menú
    if opc=="1":
        nombre=input("Ingrese el nombre: ")
        #apellido=input("Ingrese el apellido: ")
        identificacion=input("Ingrese el numero de indetificación: ")
        identificacion=proce.checka(identificacion) #revisa si el numero esta repetido y si es un numero
        edad=input("Ingrese la edad: ")
        edad=proce.esnum(edad) #Revisa si la edad es un numero
        #correo=input("Ingrese el correo: ")
        #ocupacion=input("Ingrese la ocupación: ")
        #genero=input("Ingrese el genero: ") #aca se le piden los datos al cliente
        perso=Persona(nombre,edad,identificacion) #se crea el objeto perso con los atributos que brindó el cliente
        print("Datos de la persona: ")
        perso.mostrardatos() #se usa definición mostrar datos para mostrar los datos que se acabaron de ingresar
        proce.addper(perso) #Se añade el objeto a la lista en AdminDatos
        
    elif opc=="2":
        print("testy")

    elif opc=="4": #para mostrar los datos de todas las personas
        proce.mostrar()
    elif opc=="3": #Permite eliminar los datos ingresando el numero de la persona, siendo el numero el orden en el cual salen al mostrar toda la lista
        proce.mostrar()
        numero=int(input("Ingrese la posicion de la persona que desea eliminar: "))
        proce.borrar(numero)

    elif opc=="5":
        proce.buscar()

    elif opc=="0":
        break
    else:
        print("Opción invalida")
print("Adios")


#stail