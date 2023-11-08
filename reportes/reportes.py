import sqlite3
from datetime import date, timedelta

def cantidadLibrosXEstado():
    conn = sqlite3.connect("./biblioteca.db")
    cursor = conn.cursor()
    cursor.execute('''SELECT estado, COUNT(*) AS cantidad FROM libros GROUP BY estado''')

#Devuelve listado REVISAR Y HACER VISUALES
    resultado = cursor.fetchall()

    conn.commit()
    conn.close()

    return print(resultado)

def sumatoriaPrecioRepLibrosExtraviados():
    conn = sqlite3.connect("./biblioteca.db")
    cursor = conn.cursor()
    cursor.execute('''SELECT sum(l.precioReposicion) as sumaTotal FROM libros l where l.estado="Extraviado"''')

#Devuelve listado REVISAR Y HACER VISUALES
    resultado = cursor.fetchall()

    conn.commit()
    conn.close()

    return print(resultado)

def solicitantesLibroXTitulo(titulo):
    conn = sqlite3.connect("./biblioteca.db")
    cursor = conn.cursor()
    sql = '''SELECT s.nombre, s.apellido FROM prestamos p, libros l, socios s WHERE p.idCliente=s.idCliente and p.codigoLibro=l.codigo and l.titulo=?'''
    cursor.execute(sql, (titulo,))

#Devuelve listado REVISAR Y HACER VISUALES
    resultado = cursor.fetchall()

    conn.commit()
    conn.close()

    return print(resultado)

def prestamosDeSocio(idSocio):
    conn = sqlite3.connect("./biblioteca.db")
    cursor = conn.cursor()
    sql = '''SELECT p.* FROM prestamos p, socios s WHERE p.idCliente=s.idCliente and p.idCliente=?'''
    cursor.execute(sql, (idSocio,))

#Devuelve listado REVISAR Y HACER VISUALES
    resultado = cursor.fetchall()

    conn.commit()
    conn.close()

    return print(resultado)

def prestamosDemorados():
    conn = sqlite3.connect("./biblioteca.db")
    cursor = conn.cursor()
    cursor.execute('''SELECT p.* FROM prestamos p, libros l WHERE p.codigoLibro=l.codigo and l.estado="Prestado"''')

#Devuelve listado REVISAR Y HACER VISUALES
    resultado = cursor.fetchall()
    demorados = []
    print("res", resultado)
    for p in resultado:
        print("p", p)
        suma = timedelta(days=p[4])
        if date.today() > p[3]+suma:
            demorados.append(p)

    conn.commit()
    conn.close()

    return print(demorados)

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
