import sqlite3
from libro import Libro


"""

CREAR NUEVO LIBRO

titulo = input("Ingrese el nombre del libro: ")
precioReposicion = int(input("Ingrese el precio de reposicion: "))

nuevoLibro = Libro(titulo, precioReposicion)

conn = sqlite3.connect("./biblioteca.db")
cursor = conn.cursor()

cursor.execute('''INSERT INTO libros (titulo, precioReposicion, estado) VALUES (?, ?, ?)''', (nuevoLibro._titulo, nuevoLibro._precioReposicion, "Disponible"))
    
conn.commit()
conn.close()

"""