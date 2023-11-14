from tkinter import *
from reportes.cantidadLibrosXEstado import VentanaCantidadLibrosXEstado
from reportes.sumatoria import VentanaSumatoria
from reportes.solicitantes import VentanaSolicitantes
from reportes.prestamosDeSocio import VentanaPrestamosDeSocio
from reportes.demorados import VentanaDemorados

class VentanaReportes:
    def __init__(self):
        
        self.ventana = Tk()
        
        self.ventana.title("Reportes")
        self.ventana.geometry("600x600")
        
        botones = Frame(self.ventana)
        botones.pack(padx=10, pady=50, anchor=NW)
        
        botonLibXEstado = Button(botones, text="Cant libros por estado", width=20, height=2)
        botonLibXEstado.pack(side=TOP, padx=10, pady=5, anchor=W)   
          
        botonSumatoria = Button(botones, text="Sumatoria precio rep", width=20, height=2)     
        botonSumatoria.pack(side=TOP, padx=10, pady=5, anchor=W) 
        
        botonSolicitantes = Button(botones, text="Solicitantes libro", width=20, height=2)     
        botonSolicitantes.pack(side=TOP, padx=10, pady=5, anchor=W) 
        
        botonPrestamosSocio = Button(botones, text="Prestamos de socio", width=20, height=2)     
        botonPrestamosSocio.pack(side=TOP, padx=10, pady=5, anchor=W) 
            
        botonDemorados = Button(botones, text="Prestamos demorados", width=20, height=2) 
        botonDemorados.pack(side=TOP, padx=10, pady=5, anchor=W)

        botonCancelar = Button(text="Salir", width=20, height=2)
        botonCancelar.pack(side=RIGHT, anchor=SE, padx=10, pady=5)

        botonLibXEstado["command"] = self.cantidadLibrosXEstado
        botonSumatoria["command"] = self.sumatoriaPrecioRepLibrosExtraviados
        botonSolicitantes["command"] = self.solicitantesLibroXTitulo
        botonPrestamosSocio["command"] = self.prestamosDeSocio
        botonDemorados["command"] = self.prestamosDemorados
        botonCancelar["command"] = self.cancelar
        
    def cantidadLibrosXEstado(self):
        nuevaVentana = VentanaCantidadLibrosXEstado()
        nuevaVentana.mostrar()
    
    def sumatoriaPrecioRepLibrosExtraviados(self):
        nuevaVentana = VentanaSumatoria()
        nuevaVentana.mostrar()

    def solicitantesLibroXTitulo(self):
        nuevaVentana = VentanaSolicitantes()
        nuevaVentana.mostrar()

    def prestamosDeSocio(self):
        nuevaVentana = VentanaPrestamosDeSocio()
        nuevaVentana.mostrar()
    
    def prestamosDemorados(self):
        nuevaVentana = VentanaDemorados()
        nuevaVentana.mostrar()

    def cancelar(self):
        self.ventana.destroy()
        
    def mostrar(self):
        self.ventana.mainloop()

# def cantLibrosXEstado(self):
#     c = [0, 0, 0]
#     for l in self.libros:
#         if l.estado.lower() == "disponible":
#             c[0] += 1
#         elif l.estado.lower() == "prestado":
#             c[1] += 1
#         elif l.estado.lower() == "extraviado":
#             c[2] += 1
#     return "Cantidad de libros por estado:\nDisponible: " + c[0] + "\nPrestado: " + c[1] + "\nExtraviado: " + c[2]
#
# def sumatoriaPrecioRep(self):
#     c = 0
#     for l in self.libros:
#         if l.estado.lower() == "extraviado":
#             c += l.precioReposicion
#     return "Sumatoria de precio de reposicion:\n" + c
#
# def solicitantesDeLibro(self, libro):
#     pass
#
# def prestamosDeSocio(self, nroSocio):
#     prestamos = []
#     for s in self.socios:
#         if s.idCliente == nroSocio:
#             for p in self.prestamos:
#                 if p.socio == s:
#                     prestamos.append(p)
#     if prestamos.len()==0:
#     return prestamos
#
#
# def prestamosDemorados(self):
#     demorados = []
#     for p in self.prestamos:
#         if p.esDemorado():
#             demorados.append(p)
#     return demorados
