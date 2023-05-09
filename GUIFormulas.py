import math
from tkinter import *
from tkinter import messagebox


class VentanaPrincipal(Tk):
    
    def __init__(self):
        super().__init__()
        self.config(width=500, height=300,bg="white smoke")
        self.title("Resolvedor de formulas")
        self.crearBotones(["CARGA PUNTUAL", "FRANJA CARGA", "CARGA TRIANGULAR",
                           "CARGA CIRCULAR", "CARGA TERRAPLEN", "CARGA RECTANGULAR"])
    

    def crearBotones(self, botones):
        for i, nombre in enumerate(botones):
            boton = Button(self, text=nombre, width=40, height=10,bg="gainsboro",border=0,command=lambda n=nombre:self.abrirVentana(n))
            boton.grid(row=i // 3, column=i % 3, padx=20, pady=20)
    
    def abrirVentana(self, nombre):
        self.ventana = ventanasFormulas(nombre)
        
        
class ventanasFormulas(Toplevel):
    listaPuntual = []
    listaCarga = []
    listaTriangular = []
    listaTerraplen = []
    listaCircular = []
    listaRectangular = []
    
    def __init__(self, titulo):
        super().__init__()
        self.config(width=400, height=500,bg="white smoke")
        self.title(titulo)
        self.focus()
        self.grab_set()
        self.listaPuntual.clear()
        self.listaCarga.clear()
        self.listaTriangular.clear()
        self.listaTerraplen.clear()
        self.listaCircular.clear()
        self.listaRectangular.clear()
        self.personalizarVentana(titulo)

    def personalizarVentana(self, nombre): 
        
        if nombre == "CARGA PUNTUAL":
            self.colocarEntradas(["Valor carga puntual (Kn)", "Distancia horizontal de carga al punto (M)",
                                  "Valor de la profundidad (M)"], nombre)
        elif nombre == "FRANJA CARGA":
            self.colocarEntradas(["Valor de la carga (Kn)", "valor de la mitad de la longitud de la carga (M)",
                                  "Valor de la profundidad (M)",
                                  "Valor de la distancia desde el final de la franja hasta el punto (M)"], nombre)
        elif nombre == "CARGA TRIANGULAR":
            self.colocarEntradas(["valor de la carga puntual (Kn)", "valor de la profundidad (M)",
                                  "valor de la mitad de la longitud de la carga (M)",
                                  "valor de la distancia desde el final de la franja hasta el punto (M)"], nombre) 
        elif nombre == "CARGA CIRCULAR":
            self.colocarEntradas(["valor de la carga puntual (Kn)", "valor de la profundidad (M)",
                                  "valor del radio de la carga (M)"], nombre)         
        elif nombre == "CARGA TERRAPLEN":
            self.colocarEntradas(["valor del peso especifico (Kn/m3)", "valor de la altura del terraplen (M)",
                                  "valor de la profundidad (M)",
                                  "valor de la base de la parte cuadrada (M)",
                                  "valor de la base de la parte triangular (M)"], nombre)   
        elif nombre == "CARGA RECTANGULAR":
            self.colocarEntradas(["valor de la carga puntual (Kn)", "valor del area (M2)",
                                  "valor de la profundidad (M)",
                                  "valor de la base (M)",
                                  "valor de la altura (M)"], nombre)  
        
    def colocarEntradas(self, entradas, nom):
        for i, nombre in enumerate(entradas):
            Label(self, text=nombre).grid(row=i + 1, column=1, padx=5, pady=5)
            entrada = Entry(self)
            entrada.grid(row=i + 1, column=2, padx=5, pady=5)
            self.llenarListas(nom, entrada)
        else:
            self.botonResult = Button(self, text="Resolver", command=lambda n=nom:self.calcular(n))
            self.botonResult.grid(row=len(entradas) + 1, column=2, padx=5, pady=5)
            self.resultados = Text(self, width=45, height=15)
            self.resultados.grid(row=len(entradas) + 2, column=0, padx=5, pady=5, columnspan=3)
            scroll = Scrollbar(self, command=self.resultados.yview)
            scroll.grid(row=len(entradas) + 2, column=3, sticky="nsew")
            self.resultados.config(yscrollcommand=scroll.set)
            
    def calcular(self, n):
        try:
        
            if n == "CARGA PUNTUAL":
                p = float(self.listaPuntual[0].get())
                r = float(self.listaPuntual[1].get())
                z = float(self.listaPuntual[2].get())
                
                r = self.cargaPuntual(p, r, z)
                
                self.resultados.insert("end", f"{r[0]}\n")
                self.resultados.insert("end", f"{r[1]}\n\n")
                
            elif n == "FRANJA CARGA":
                
                q = float(self.listaCarga[0].get())
                z = float(self.listaCarga[1].get())
                b = float(self.listaCarga[2].get())
                a = float(self.listaCarga[3].get())
                
                r = self.cargaFranja(q, z, b, a)
                
                self.resultados.insert("end", f"{r[0]}\n")
                self.resultados.insert("end", f"{r[1]}\n")
                self.resultados.insert("end", f"{r[2]}\n\n")
                
            elif n == "CARGA TRIANGULAR":
                q = float(self.listaTriangular[0].get())
                z = float(self.listaTriangular[1].get())
                b = float(self.listaTriangular[2].get())
                a = float(self.listaTriangular[3].get())
                
                r = self.cargaTriangular(q, z, b, a)
                
                self.resultados.insert("end", f"{r[0]}\n")
                self.resultados.insert("end", f"{r[1]}\n\n")
                
            elif n == "CARGA CIRCULAR":
                q = float(self.listaCircular[0].get())
                z = float(self.listaCircular[1].get())
                a = float(self.listaCircular[2].get())
                
                r = self.cargaCircular(q, z, a)
                self.resultados.insert("end", f"{r}\n\n")
            elif n == "CARGA TERRAPLEN":
                gama = float(self.listaTerraplen[0].get())
                h = float(self.listaTerraplen[1].get())
                z = float(self.listaTerraplen[2].get())
                b1 = float(self.listaTerraplen[3].get())
                b2 = float(self.listaTerraplen[4].get())
                
                r = self.cargaTerraplen(gama, h, z, b1, b2)
                self.resultados.insert("end", f"{r}\n\n")
    
            elif n == "CARGA RECTANGULAR":
                q = float(self.listaRectangular[0].get())
                a = float(self.listaRectangular[1].get())
                z = float(self.listaRectangular[2].get())
                b = float(self.listaRectangular[3].get())
                l = float(self.listaRectangular[4].get())
                
                r = self.cargaRectangular(q, a, z, b, l)
                self.resultados.insert("end", f"{r[0]}\n")
                self.resultados.insert("end", f"{r[1]}\n\n")
        except:
            messagebox.showwarning("Cuidado", "ERROR: NO INTRODUZCA TEXTO NI DEJE ESPACIOS EN BLANCO")
        
    def cargaRectangular(self, q, a, z, b, l): 
        pi = math.pi
        qd = float(q) / float(a)  # carga distribuida
        resultado1 = 'carga distribuida (qd) = %5.3f Kn/m2 ' % (qd)
        m = float(b) / float(z)
        n = float(l) / float(z)
        t1 = ((2 * m * n) * ((m ** 2) + (n ** 2) + 1) ** 0.5) / ((m ** 2) + (n ** 2) + (m ** 2) * (n ** 2) + 1)
        t2 = ((m ** 2) + (n ** 2) + 2) / ((m ** 2) + (n ** 2) + 1)
        if (m ** 2) + (n ** 2) + 1 < (m ** 2) * (n ** 2):
            t3 = math.atan(pi + ((2 * m * n) * ((m ** 2) + (n ** 2) + 1) ** 0.5) / ((m ** 2) + (n ** 2) - (m ** 2) * (n ** 2) + 1))
        else: 
            t3 = math.atan(((2 * m * n) * ((m ** 2) + (n ** 2) + 1) ** 0.5) / ((m ** 2) + (n ** 2) - (m ** 2) * (n ** 2) + 1))
        Iz = (1 / (4 * pi)) * (t1 * t2 + t3)
        sigmazr = qd * Iz
        resultado2 = 'sigmazr = %5.3f Kn/m2 ' % (sigmazr)
        
        rs = (resultado1, resultado2)
        
        return rs
             
    def cargaCircular(self, q, z, a):
        sigmazc = float(q) * (1 - (1 / (1 + (float(a) / float(z)) ** 2) ** 1.5))
        resultado = 'sigmazc = %5.3f Kn/m2 ' % (sigmazc)
        
        return resultado

    def cargaTerraplen(self, gama, h, z, b1, b2): 
        q0 = float(gama) * float(h)  # en Kn/m2
        pi = math. pi
        alpha1 = math.atan(float(b1) / float(z))
        beta = math.atan((float(b1) + float(b2)) / float(z))
        alpha2 = beta - alpha1
        sigmazterraplen = (q0 / pi) * (((float(b1) + float(b2)) / float(b2)) * (alpha1 + alpha2) - ((float(b1) / float(b2)) * (alpha2)))
        resultado = 'sigmazterraplen = %5.3f Kn/m2 ' % (sigmazterraplen)
        return resultado

    def cargaPuntual(self, p, r, z):
        pi = math.pi
        rz2 = (float(r) / float(z)) ** 2
        i = (3 / (2 * pi)) * (1 / ((rz2) + 1) ** 2.5)
        resultado1 = 'i = %5.3f  ' % (i)
        sigmazp = (float(p) / (float(z) ** 2)) * i  # en kn/m
        resultado2 = 'sigmazp = %5.3f kn/m2 ' % (sigmazp)
        
        rs = (resultado1, resultado2)
        
        return rs

    def cargaTriangular(self, q, z, b, a):
        B = 2 * float(b)
        x = B + float(a)
        beta = math.atan(float(a) / float(z))  # en radianes
        delta = math.atan(x / float(z))  # en radianes
        alpha = delta - beta  # en radianes
        pi = math. pi
        sigmaxt = (float(q) / (2 * pi)) * (((alpha * x) / float(b)) - (math.sin(2 * beta)))
        resultado = 'sigmaxt = %5.3f Kn/m2 ' % (sigmaxt)
        taoxzt = (float(q) / (2 * pi)) * (1 + (math.cos(2 * beta)) - ((float(z) * alpha) / float(b)))
        resultado2 = 'taoxzt = %5.3f Kn ' % (taoxzt)
        
        rs = (resultado, resultado2)
        return rs

    def cargaFranja(self, q, z, b, a):
        B = 2 * float(b)
        # B es la longitud total de la franja 
        c = float(B) + float(a)
        delta = math.atan(float(a) / float(z))  # en radianes
        beta = math.atan(float(c) / float(z))  # en radianes
        alpha = beta - delta  # en radianes
        pi = math. pi
        sigmazf = (float(q) / pi) * (alpha + math.sin(alpha) * math.cos(alpha + 2 * delta))  # en kn/m
        resultado1 = 'sigmazf = %5.3f kn/m2 ' % (sigmazf)
        sigmaxf = (float(q) / pi) * (alpha - math.sin(alpha) * math.cos(alpha + 2 * delta))  # en kn/m
        resultado2 = 'sigmaxf = %5.3f kn/m2 ' % (sigmaxf)
        taof = (float(q) / pi) * (math.sin(alpha) * math.sin(alpha + 2 * delta))  # en kn/m
        resultado3 = 'taof = %5.3f kn ' % (taof)
        
        rs = (resultado1, resultado2, resultado3)
        
        return rs
        
    def llenarListas(self, nombre, fieldText):
        if nombre == "CARGA PUNTUAL":
            self.listaPuntual.append(fieldText)
        elif nombre == "FRANJA CARGA":
            self.listaCarga.append(fieldText)
        elif nombre == "CARGA TRIANGULAR":
            self.listaTriangular.append(fieldText)
        elif nombre == "CARGA CIRCULAR":
            self.listaCircular.append(fieldText)
        elif nombre == "CARGA TERRAPLEN":
            self.listaTerraplen.append(fieldText)
        elif nombre == "CARGA RECTANGULAR":
            self.listaRectangular.append(fieldText)

    
miVentanaP = VentanaPrincipal()

miVentanaP.mainloop()        
