import pickle
from Serializacion.Estudiantes import *


estu1 = Estudiantes("Gabriel","Sistemas",19)
estu2 = Estudiantes("Antonio","Psicologia",23)
estu3 = Estudiantes("Palvin","Negocios",27)

'''lista = ListaEstudiantes()

lista.agregarEstudiantes(estu1)
lista.agregarEstudiantes(estu2)
lista.agregarEstudiantes(estu3)'''

lista = ListaEstudiantes().get_estudiantes()

for e in lista:
    print(e)