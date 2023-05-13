from tkinter import *
from tkinter import messagebox
from Principal.Controlador import Controlador

class vprincipal(Tk):
    def __init__(self):
        super().__init__()
        self.config(width=400,height=500)
        self.frameCentro = Frame(self,width=300,height=300)
        self.frameCentro.pack()
        self.frameDown = Frame(self,width=300,height=50)
        self.frameDown.pack()
        self.barraMenu = Menu(self)
        self.bbddMenu = self.crearBarra(1)
        self.borrar = self.crearBarra(2)
        self.CRUD = self.crearBarra(3)
        self.acercaDe = self.crearBarra(4)
        self.config(menu=self.barraMenu)
        
        labels=("id","nombre","password","direccion","comentarios")
        self.crearCuerpo(labels)
        self.controlador = Controlador(self)
        botones=("LEER","INSERTAR","ACTUALIZAR","BORRAR")
        self.crearBotones(botones)
        self.crearAcciones()
        
    
    def mensajeInsertar(self,numero):
        
        messagebox.showinfo("Confirmacion", "Se ha añadido correctamente")
        
        
    def mensajeActualizar(self):
        messagebox.showinfo("Confirmacion", "Se ha Actualizado correctamente")    
    
    def mensajeEliminar(self):
        messagebox.showinfo("Confirmacion", "Se ha borrado correctamente")    
        
    def crearBarra(self,numero):
        subMenu = Menu(self.barraMenu,tearoff=0)
        if numero == 1:
            subMenu.add_command(label="Salir",command=lambda:self.destroy())
        elif numero==2:
            subMenu.add_command(label="Borrar",command=lambda:self.borrarE())
        elif numero==3:
            subMenu.add_command(label="Crear",command=lambda:self.controlador.controlarRegistro())
            subMenu.add_command(label="Leer",command=lambda:self.controlador.controlarListaUsuarios())
            subMenu.add_command(label="Actualizar",command=lambda:self.controlador.controlarActualizar())
            subMenu.add_command(label="Eliminar",command=lambda:self.controlador.controlarEliminar())        
        elif numero==4:
            subMenu.add_command(label="Acerca de")
        
        listaLabels = ["Opciones","Limpiar","CRUD","More"]
        self.barraMenu.add_cascade(label=listaLabels[numero-1],menu=subMenu)
        return subMenu
        
    def crearCuerpo(self,labels):
        listaEntry = []
        for i, e in enumerate(labels):
            
            if i != len(labels)-1:
                Label(self.frameCentro,text=e).grid(row=i+1,column=0,padx=5,pady=5)
                entrada = Entry(self.frameCentro)
                entrada.grid(row=i+1,column=1,padx=5,pady=5)
                listaEntry.append(entrada)
            else:
                Label(self.frameCentro,text=e).grid(row=i+1,column=0,padx=5,pady=5)
                entrada = Text(self.frameCentro,width=25,height=15)
                entrada.grid(row=i+1,column=1,padx=5,pady=5)
                scroll = Scrollbar(self.frameCentro, command=entrada.yview)
                scroll.grid(row=i+1, column=2, sticky="nsew")
                entrada.config(yscrollcommand=scroll.set)
                listaEntry.append(entrada)    
        else:
            self.txtId= listaEntry[0]
            self.txtNombre = listaEntry[1]
            self.txtPassword= listaEntry[2]
            self.txtDire = listaEntry[3]
            self.txtComentarios= listaEntry[4]
            
    def crearBotones(self,botonesNombre):    
        listaBotones = []
        for i, b in enumerate(botonesNombre):
            btn = Button(self.frameDown,text=b,width=10,height=2)
            btn.grid(row=0,column=i+1,padx=5,pady=5)
            listaBotones.append(btn)
        else:
            self.btnLeer=listaBotones[0]
            self.btnInsertar=listaBotones[1]
            self.btnActualizar=listaBotones[2]
            self.btnBorrar=listaBotones[3]
            
    def crearAcciones(self):
        self.btnLeer.config(command=lambda:self.controlador.controlarObtener()) 
        self.btnBorrar.config(command=lambda:self.controlador.controlarEliminar())
        self.btnInsertar.config(command=lambda:self.controlador.controlarRegistro())
        self.btnActualizar.config(command=lambda:self.controlador.controlarActualizar())

    def borrarE(self):
        self.txtNombre.delete(0, END)
        self.txtPassword.delete(0, END)
        self.txtDire.delete(0, END)
        self.txtComentarios.delete("1.0", END)    
               
    
    def mostrarTodos(self,listaUsuarios):
        ventanaTodos = Toplevel()
        ventanaTodos.title("todos los registros")    
        ventanaTodos.config(width=70,height=30)
        texto= Text(ventanaTodos,width=70,height=30)
        texto.grid(row=0, column=1)
        scroll = Scrollbar(ventanaTodos, command=texto.yview)
        scroll.grid(row=0, column=2, sticky="nsew")
        texto.config(yscrollcommand=scroll.set)
        
        usuarios = listaUsuarios
        
        for usuario in usuarios:
            texto.insert("end", f"{usuario}\n")
        
           
v = vprincipal()

v.mainloop()
        
        