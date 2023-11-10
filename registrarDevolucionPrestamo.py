from tkinter import *
import sqlite3
from tkinter import messagebox

def registrarDevolucionBD(codigo):
    conn = sqlite3.connect("./biblioteca.db")
    cursor = conn.cursor()
    sql = '''SELECT p.codigoLibro FROM Prestamos p WHERE p.codigoPrestamo = ?'''
    cursor.execute(sql, (codigo))
    
    codigoLibro = cursor.fetchall()
    codigo.split(",")
    
    actualizacionEstadoSQL = '''UPDATE libros SET estado = "Disponible" WHERE codigo = ?'''
    cursor.execute(actualizacionEstadoSQL, (codigoLibro[0]))
    
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Exito", "Devolucion registrada correctamente")

class VentanaRegistrarDevolucion:
    def __init__(self):
        
        self.ventana = Tk()
        self.ventana.title("Registrar devolucion de libro")
        self.ventana.geometry("600x600")
        
        
        Label(self.ventana, text="Codigo de prestamo: ").grid(column=0, row=0, padx=10, pady=10, sticky="e")
        self.txt_codigoPrestamo = Entry(self.ventana, width=40)
        self.txt_codigoPrestamo.grid(column=1, row=0, sticky="w")

        
        botones = Frame(self.ventana)
        botones.grid(column=1, row=4, sticky="e")
        
        botonCancelar = Button(botones, text="Cancelar")
        botonCancelar.pack(side="right", padx=10)
        
        botonAceptar = Button(botones, text="Aceptar")
        botonAceptar.pack(side="right")
        
        botonAceptar["command"] = self.aceptar
        botonCancelar["command"] = self.cancelar
    
    def aceptar(self):
        codigo = self.txt_codigoPrestamo.get()
        if not codigo:
            messagebox.showerror("Error", "Ingrese un codigo de prestamo.")
        else:
            registrarDevolucionBD(codigo)
    
    def cancelar(self):
        self.ventana.destroy()
        
    def mostrar(self):
        self.ventana.mainloop()
        
VentanaRegistrarDevolucion().mostrar()