from Principal.Modelo import Modelo
from Principal.Modelo import Usuario
import tkinter as tk
import traceback



class Controlador():
    def __init__(self,vista):
        self.miVista = vista
        
        
    def controlarRegistro(self):
        nombre = self.miVista.txtNombre.get()
        password = self.miVista.txtPassword.get()
        direccion = self.miVista.txtDire.get()
        comentarios = self.miVista.txtComentarios.get("1.0",tk.END)
        
        u = Usuario(nombre,password,direccion,comentarios)
        
        try:
            modelo = Modelo()
            modelo.insertar(u)
            self.miVista.borrarE()
            self.miVista.mensajeInsertar()
        except:
            traceback.print_exc()    
        
    
    def controlarListaUsuarios(self):
        try:
            modelo = Modelo()
            listaUsuarios = modelo.listarUsuarios()
            self.miVista.mostrarTodos(listaUsuarios)
        except:
            traceback.print_exc()
        
    def controlarActualizar(self):
        
        aid = int(self.miVista.txtId.get())
        nombre = self.miVista.txtNombre.get()
        password = self.miVista.txtPassword.get()
        direccion = self.miVista.txtDire.get()
        comentarios = self.miVista.txtComentarios.get("1.0",tk.END)
        u = Usuario(nombre,password,direccion,comentarios)
        
        
        try:
            modelo = Modelo()
            
            
            modelo.actualizar(u, aid)
            
            self.miVista.borrarE()
            self.miVista.mensajeActualizar()
        except:
            traceback.print_exc()    
        
        
    def controlarObtener(self):
        print("estyo aca")
        try:
            id = int(self.miVista.txtId.get())
            
            modelo = Modelo()

            usuario = modelo.obtenerUsuario(id)
            self.miVista.borrarE()
            self.miVista.txtNombre.insert(0,usuario.get_nombre())
            self.miVista.txtPassword.insert(0,usuario.get_password())
            self.miVista.txtDire.insert(0,usuario.get_direccion())
            self.miVista.txtComentarios.insert("end",usuario.get_comentarios())
        except:
            print("HA OCURRIDO UN ERROR")    
            traceback.print_exc()

        
    def controlarEliminar(self):                
        
        
        try:
            modelo = Modelo()
            
            did = int(self.miVista.txtId.get())
            
            modelo.eliminarUsuario(did)
            self.miVista.borrarE()
            self.miVista.mensajeEliminar()
        except:
            traceback.print_exc()
        
        