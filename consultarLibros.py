import tkinter as tk
import sqlite3

"""
def consultar_clientes():
    
    nombre = entrada_nombre.get()
   
    resultado_consulta = ["Cliente 1", "Cliente 2", "Cliente 3"]
    
   
    grilla.delete(0, tk.END)
    
    
    for cliente in resultado_consulta:
        grilla.insert(tk.END, cliente)

ventana = tk.Tk()
ventana.title("Consulta de Clientes")


etiqueta_nombre = tk.Label(ventana, text="Nombre del Cliente:")
etiqueta_nombre.pack()


entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()


boton_consultar = tk.Button(ventana, text="Consultar", command=consultar_clientes)
boton_consultar.pack()

grilla = tk.Listbox(ventana)
grilla.pack()

ventana.mainloop()
"""


def consultarLibrosBD(entradaTitulo):
    
    libro = entradaTitulo.get()
    
    conn = sqlite3.connect("S:\Documents\Documentos Ema\DAO\TP Dao\biblioteca.db")
    cursor = conn.cursor()
    sql = '''SELECT l.codigo, l.titulo, l.precioReposicion, l.estado From libros l WHERE l.titulo = ?'''
    cursor.execute(sql, (libro))
    
    resultado = cursor.fetchall()
    
    for libro in resultado:
        grilla.insert(tk.END, libro)
        
    conn.commit()
    conn.close()

def consultarLibros():
    
    ventanaConsultarLibros = tk.Tk()
    ventanaConsultarLibros.title("Consultar libros")
    
    labelLibro = tk.Label(ventanaConsultarLibros, text="Titulo del libro: ")
    labelLibro.pack()
    
    entradaTitulo = tk.Entry(ventanaConsultarLibros)
    entradaTitulo.pack()
    
    botonConsultar = tk.Button(ventanaConsultarLibros, text="Consultar", command=consultarLibrosBD(entradaTitulo))
    botonConsultar.pack()
    
    grilla = tk.Listbox(ventanaConsultarLibros)
    grilla.pack()
    
    ventanaConsultarLibros.mainloop()

consultarLibros()