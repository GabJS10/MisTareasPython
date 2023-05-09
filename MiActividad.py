class Estudiante():
    def __init__(self,nombre,carrera,edad):
        self.__nombre = nombre
        self.__carrera= carrera
        self.__edad= edad
    
    
    def get_nombre(self):
        return (self.__nombre)

    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def get_carrera(self):
        return (self.__carrera)

    def set_carrera(self, carrera):
        self.__carrera= carrera    
    
    def get_edad(self):
        return (self.__edad)

    def set_edad(self, edad):
        self.__edad = edad
        



def dameMenu():
    opciones={"1":"CREAR ESTUDIANTE",
              "2":"LISTAR ESTUDIANTE",
              "3":"BUSCAR ESTUDIANTE",
              "4":"ELIMINAR ESTUDIANTE",
              "5":"SALIR"
              }
    return opciones


def mostrarMenu(menu):
    for (clave,valor) in menu.items():
        print(f"{clave}:{valor}") 
    else:
        print("")   


def mostrarEstudiantes(listaEstudiantes):
    print("NOMBRE - CARRERA - EDAD")

    for e in listaEstudiantes:
        print(f"{e.get_nombre()} -{e.get_carrera()} - {e.get_edad()} ")
    else:
        print("")    
        
def buscarEstudiantes(listaEstudiantes,nombre):
    existe=False;
    
    for e in listaEstudiantes:
        if(e.get_nombre() == nombre):
            print("NOMBRE - CARRERA - EDAD")
            print(f"{e.get_nombre()} -{e.get_carrera()} - {e.get_edad()} ")
            existe=True
            break
    else:
        
        print("") 
    
    if not existe:
        print("EL ESTUDIANTE NO EXISTE")
         
def eliminar(listaEstudiantes,nombre):
    for e in listaEstudiantes:
        if(e.get_nombre() == nombre):
            listaEstudiantes.remove(e)
            print("estudiante eliminado")
            break        
lista = []        
while True:
    mostrarMenu(dameMenu())
    opcionElegida=input("SELECCIONE UNA OPCION: ")
    if opcionElegida == str(5):
        break     
    elif opcionElegida == str(1):
        n=input("NOMBRE DEL ESTUDIANTE: ")
        c=input("CARRERA DEL ESTUDIANTE: ")
        e=int(input("EDAD DEL ESTUDIANTE: "))
        estudiante = Estudiante(n,c,e)
        lista.append(estudiante)
    elif opcionElegida == str(2):
        mostrarEstudiantes(lista)
    elif opcionElegida == str(3):
        nombre=input("NOMBRE DEL ESTUDIANTE A BUSCAR: ")
        buscarEstudiantes(lista,nombre)
    elif opcionElegida == str(4):
        nombre=input("NOMBRE DEL ESTUDIANTE A ELIMINAR: ")
        eliminar(lista, nombre)
    else:
        print("SELECCIONE UNA OPCION CORRECTA")        
print("fin")    