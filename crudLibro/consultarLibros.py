from tkinter import *
import sqlite3

def consultarLibrosBD(titulo):
    
    conn = sqlite3.connect("./biblioteca.db")
    cursor = conn.cursor()
    sql = '''SELECT l.* From libros l WHERE l.titulo = ?'''
    cursor.execute(sql, (titulo))
    
    resultado = cursor.fetchall()
    
    libros = []
    for libro in resultado:
        libros.append(libro)
        
    conn.commit()
    conn.close()
    
    return libros

class VentanaConsultarLibro:
    def __init__(self):
        
        self.ventana = Tk()
        
        self.ventana.title("Consultar libro")
        self.ventana.geometry("600x600")
        
        Label(self.ventana, text="Titulo").grid(column=0, row=0, padx=10, pady=10, sticky="e")
        
        self.txt_titulo = Entry(self.ventana, width=40)
        self.txt_titulo.grid(column=1, row=0, sticky="w")
        
        Listbox(self.ventana).grid(column=1, row=1, sticky="w")
        
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
        consultarLibrosBD(titulo)
        
        
    def cancelar(self):
        self.ventana.quit()
        
    
    def mostrar(self):
        self.ventana.mainloop()
        
VentanaConsultarLibro().mostrar()