from tkinter import Tk, Label, Entry, Button, Frame, ttk
import sqlite3
from tkinter import messagebox

def consultarLibrosBD(titulo):
    
    conn = sqlite3.connect("./biblioteca.db")
    cursor = conn.cursor()
    sql = '''SELECT l.* From libros l WHERE l.titulo = ?'''
    cursor.execute(sql, (titulo,))
    
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
        
        self.tree = ttk.Treeview(self.ventana, show='headings', columns=('ID', 'Titulo', 'PrecioReposicion', 'Estado'))
        self.tree.heading('#1', text='ID')
        self.tree.heading('#2', text='Titulo')
        self.tree.heading('#3', text='PrecioReposicion')
        self.tree.heading('#4', text='Estado')
        self.tree.column('#1', minwidth=50, width=50, anchor="center")
        self.tree.column('#2', minwidth=50, width=200, anchor="center")
        self.tree.column('#3', minwidth=50, width=125, anchor="center")
        self.tree.column('#4', minwidth=50, width=100, anchor="center")
        self.tree.grid(column=1, row=1, sticky="w")
        
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
        if not titulo:
            messagebox.showerror("Error", "Ingrese el titulo de un libro a buscar.")
        else:
            datosLibro = consultarLibrosBD(titulo)
            for row in self.tree.get_children():
                self.tree.delete(row)
            for libro in datosLibro:
                self.tree.insert('', 0, values=libro)
            
        
        
    def cancelar(self):
        self.ventana.destroy()
        
    
    def mostrar(self):
        self.ventana.mainloop()