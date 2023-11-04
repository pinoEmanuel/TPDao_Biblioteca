import tkinter as tk
import sqlite3

def consultarSocioBD(entradaId):
    
    idCliente = entradaId.get()
    
    conn = sqlite3.connect("./biblioteca.db")
    cursor = conn.cursor()
    
    sql = '''SELECT s.* From socios s WHERE s.idCliente = ?'''
    cursor.execute(sql, (idCliente))
    
    resultado = cursor.fetchall()
    
    grilla.insert(tk.END, resultado)
    
    conn.commit()
    conn.close()

def consultarSocio():
    
    ventanaConsultarSocio = tk.Tk()
    ventanaConsultarSocio.title("Consultar socios.")
    
    labelSocio = tk.Label(ventanaConsultarSocio, text="ID del cliente a buscar")
    labelSocio.pack()
    
    entradaId = tk.Entry(ventanaConsultarSocio)
    entradaId.pack()
    
    botonConsultar = tk.Button(ventanaConsultarSocio, text="Consultar", command=consultarSocioBD(entradaId))
    botonConsultar.pack()
    
    grilla = tk.Listbox(ventanaConsultarSocio)
    grilla.pack()
    
    ventanaConsultarSocio.mainloop()
    
consultarSocio()