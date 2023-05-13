import mysql.connector
import traceback


class Usuario():
    def __init__(self,nombre,password,direccion,comentarios):
        self.__nombre = nombre
        self.__password= password
        self.__direccion= direccion
        self.__comentarios = comentarios
        
    
    def __str__(self):
        return f" Nombre: {self.__nombre}, Password: {self.__password}, Direccion: {self.__direccion}, Comentarios: {self.__comentarios}"

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    def get_direccion(self):
        return self.__direccion

    def set_direccion(self, direccion):
        self.__direccion = direccion

    def get_comentarios(self):
        return self.__comentarios

    def set_comentarios(self, comentarios):
        self.__comentarios = comentarios
        

class Modelo():
    
    def __init__(self):
        self.conexion=None
        
    
    def getConnection(self):
        if self.conexion is None:
            try:
                self.conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="crudpython"
                )
            except mysql.connector.Error as error:
                print("ERROR AL CONECTAR " + error)
                return None
        
        return self.conexion
    
            
    def listarUsuarios(self):
        
        miConexion = self.getConnection()
        
        if miConexion is None:
            return None
        
        try:
                
            cursor = miConexion.cursor()
            cursor.execute("SELECT * FROM usuarios")
            rs = cursor.fetchall()
            return rs
    
        except:
                print("ERROR AL LISTAR")
                traceback.print_exc()
        finally:
            cursor.close()
            miConexion.close()
    
    
    def eliminarUsuario(self,uid):
        miConexion = self.getConnection()
        
        if miConexion is None:
            return
        try:
            cursor = miConexion.cursor()
            sql = "DELETE FROM usuarios WHERE id=%s"
            cursor.execute(sql,(uid,))
            miConexion.commit()
        except:
                print("ERROR AL ELIMINAR")
                traceback.print_exc()
        finally:            
            cursor.close()
            miConexion.close()
    
    def insertar(self,Usuario):
        
        miConexion = self.getConnection()
        
        if miConexion is None:
            return
            
        try:
            sql = "INSERT INTO usuarios (nombre,password,direccion,comentarios) values (%s,%s,%s,%s)"
            datos = (Usuario.get_nombre(),Usuario.get_password(),Usuario.get_direccion(),Usuario.get_comentarios())
            
            
            cursor = miConexion.cursor()
            cursor.execute(sql,datos)
            miConexion.commit()
        except:
                print("ERROR AL AGREGAR")
                traceback.print_exc()
                
        finally:            
            cursor.close()
            miConexion.close()
        
    def actualizar(self,Usuario,uid):
        
        miConexion = self.getConnection()
        
        if miConexion is None:
            return
            
        try:
            sql="UPDATE usuarios SET nombre=%s,password=%s,direccion=%s,comentarios=%s WHERE id=%s"    
            datos=(Usuario.get_nombre(),Usuario.get_password(),Usuario.get_direccion(),Usuario.get_comentarios(),uid)
        
            
            cursor = miConexion.cursor()
            cursor.execute(sql,datos)
            miConexion.commit()
        except:
                print("ERROR AL ACTUALIZAR")
                traceback.print_exc()
                
        finally:            
            cursor.close()
            miConexion.close()
        
        
    def obtenerUsuario(self,uid):
        miConexion = self.getConnection()
        usuario = None
        if miConexion is None:
            return None
            
        try:
            print("si conexion")
            sql="SELECT * FROM usuarios WHERE id=%s"
            cursor = miConexion.cursor()
            cursor.execute(sql,(uid,))
            u = cursor.fetchone()
            nombre=u[1]
            password=u[2]
            direccion=u[3]
            comentarios=u[4]
            usuario = Usuario(nombre,password,direccion,comentarios)
        except:
                print("ERROR AL OBTENER")
                traceback.print_exc()

                return None
                
        finally:            
            cursor.close()
            miConexion.close()
        
        return usuario
        
        