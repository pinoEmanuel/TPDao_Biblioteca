from tkinter import *
import sqlite3
from crudLibro.consultarLibros import *
from crudSocios.consultarSocio import *
import sys
sys.path.insert(0, "..\TP Dao")
from entidades.prestamo import *

def registrarPrestamoBD(titulo, idSocio, cantDiasPrestamo):
    
    nuevoPrestamo = Prestamo(idSocio, titulo, cantDiasPrestamo)
    
    conn = sqlite3.connect("./biblioteca.db")
    cursor = conn.cursor
    
    cursor.execute(''' INSERT INTO prestamos (idCliente)''')
    conn.commit()
    conn.close()
    
class VentanaRegistrarPrestamo:
    
    def __init__(self):
        
        self.ventana = Tk()
        self.ventana.title("Registrar prestamo de libro")
        self.ventana.geometry("600x600")
        
        Label(self.ventana, text="Titulo del libro").grid(column=0, row=0, padx=10, pady=10, sticky="e")
        self.txt_titulo = Entry(self.ventana, width=40)
        
        Label(self.ventana, text="Id de cliente").grid(column=0, row=0, padx=10, pady=10, sticky="e")
        self.txt_idSocio = Entry(self.ventana, width=40)
        
        Label(self.ventana, text="Cantidad de dias de prestamo").grid(column=0, row=0, padx=10, pady=10, sticky="e")
        self.txt_cantDiasPrestamo = Entry(self.ventana, width=40)
        
        ##VER TEMA FECHA
        
        botones = Frame(self.ventana)
        botones.grid(column=1, row=4, sticky="e")
        
        botonCancelar = Button(botones, text="Cancelar")
        botonCancelar.pack(side="right", padx=10)
        
        botonAceptar = Button(botones, text="Aceptar")
        botonAceptar.pack(side="right")
        
        botonAceptar["command"] = self.aceptar
        botonCancelar["command"] = self.cancelar
        
    def aceptar(self):
        
        titulo = self.txt_titulo.get()
        libro = consultarLibrosBD(titulo)
        
        idSocio = int(self.txt_idSocio.get())
        cliente = consultarSociosBD(idSocio)
        
        cantDiasPrestamo = int(self.txt_cantDiasPrestamo.get())
        
        if (libro and cliente) is None:
            Label(self.ventana, text="El cliente no existe")
        elif libro is None:
            Label(self.ventana, text="El libro no existe")
        else:
            registrarPrestamoBD(titulo, idSocio, cantDiasPrestamo)
        
    def cancelar(self):
        self.ventana.destroy()
            
    def mostrar(self):
        self.ventana.mainloop()
VentanaRegistrarPrestamo().mostrar()