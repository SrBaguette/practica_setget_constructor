from funciones import Persona, AdministrarDatos
opc=-1
proce=AdministrarDatos()
while opc !=0:
    print("Bienvenido al menú")
    print("1. Agregar Persona \n 2. Modificar Persona \n 3. Eliminar Persona \n 4. Mostrar todas las personas \n 0. Salir")
    opc=input("Ingrese una opción: ")
    if opc=="1":
        nombre=input("Ingrese el nombre: ")
        apellido=input("Ingrese el apellido: ")
        identificacion=input("Ingrese el numero de indetificación")
        edad=input("Ingrese la edad: ")
        correo=input("Ingrese el correo: ")
        ocupacion=input("Ingrese la ocupación: ")
        genero=input("Ingrese el genero: ")
        perso=Persona(nombre,apellido,edad,correo,ocupacion,genero,identificacion)
        print("Datos de la persona: ")
        perso.mostrardatos()
        proce.addper(perso)
        
    elif opc=="2":
        print("testy")

    elif opc=="4":
        for datos in proce.mostrar():
            print("Persona #",datos,":")
            print(datos)
            print("\n")
    elif opc=="3":
        numero=int(input("Ingrese la posicion de la persona que desea eliminar: "))
        proce.borrar(numero)
    elif opc=="0":
        break
    else:
        print("Opción invalida")
print("Adios")