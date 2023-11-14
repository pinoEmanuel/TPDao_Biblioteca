# Por otro lado, cada vez que un libro es prestado se registra el socio que lo solicita y la cantidad
# de días pactados para su devolución. Cuando un libro es devuelto debe calcularse si fue devuelto en fecha o con demora, registrando si corresponde la cantidad de días de retraso.
#
# Todo libro prestado y que posea más de 30 días de demora en su devolución se considera extraviado, por lo tanto el software debe poder listar aquellos que se encuentren en tal condición para ofrecer al usuario el cambio de estado.
#
# Cuando un socio solicite un libro el software debe verificar que el socio no posea más de tres libros prestados (aunque todavía se encuentre dentro del plazo del préstamo) y que no posea ningún libro con demora en su devolución.
#
# La biblioteca requiere que el software ofrezca como mínimo las funcionalidades de:
# Administración de socios
# Administración de libros
# Registración de préstamos y devoluciones
# Registración de libros extraviados

# Reportes:
# Cantidad de libros en cada estado (tres totales)
# Sumatoria del precio de reposición de todos los libros extraviados
# Nombre de todos los solicitantes de un libro en particular identificado por su título
# Listado de préstamos de un socio identificado por su número de socio
# Listado de préstamos demorados

# Condiciones de entrega:
# Los datos deben ser almacenados en una base de datos sqlite cuyo diseño y creación es responsabilidad del grupo.
# La interfaz de usuario debe ser una interfaz gráfica con ventanas usando tkinter.
# Todos los datos ingresados por el usuario deben ser correctamente validados.
# La entrega se realiza mediante el módulo de tareas de la UV de un único archivo comprimido que incluya únicamente los archivos de código fuente, el archivo de la base de datos y el diagrama de entidad-relación.

from tkinter import *
from crudSocios.agregarSocio import VentanaAgregarSocio
from crudSocios.consultarSocio import VentanaConsultarSocio
from crudSocios.eliminarSocio import VentanaEliminarSocio
from crudLibro.agregarLibro import VentanaAgregarLibro
from crudLibro.consultarLibros import VentanaConsultarLibro
from crudLibro.eliminarLibro import VentanaEliminarLibro
from reportes.reportes import VentanaReportes
#from registrarPrestamo import VentanaRegistrarPrestamo

class VentanaMain:
    def __init__(self):
        
        self.ventana = Tk()
        
        self.ventana.title("Biblioteca")
        self.ventana.geometry("600x600")
        
        botones = Frame(self.ventana)
        botones.pack(padx=10, pady=50, anchor=NW)
        
        botonRegPrestamo = Button(botones, text="Registrar nuevo prestamo", width=20, height=2)
        botonRegPrestamo.pack(side=TOP, padx=10, pady=5, anchor=W)   
          
        botonRegCliente = Button(botones, text="Registrar socio", width=20, height=2)     
        botonRegCliente.pack(side=TOP, padx=10, pady=5, anchor=W) 
        
        botonConsultarCliente = Button(botones, text="Consultar socio", width=20, height=2)     
        botonConsultarCliente.pack(side=TOP, padx=10, pady=5, anchor=W) 
        
        botonEliminarCliente = Button(botones, text="Eliminar socio", width=20, height=2)     
        botonEliminarCliente.pack(side=TOP, padx=10, pady=5, anchor=W) 
            
        botonRegLibro = Button(botones, text="Registrar libro", width=20, height=2) 
        botonRegLibro.pack(side=TOP, padx=10, pady=5, anchor=W)
        
        botonConsultarLibro = Button(botones, text="Consultar libro", width=20, height=2) 
        botonConsultarLibro.pack(side=TOP, padx=10, pady=5, anchor=W)
        
        botonEliminarLibro = Button(botones, text="Eliminar libro", width=20, height=2) 
        botonEliminarLibro.pack(side=TOP, padx=10, pady=5, anchor=W)
        
        botonReportes = Button(botones, text="Reportes", width=20, height=2) 
        botonReportes.pack(side=TOP, padx=10, pady=5, anchor=W)
        
        botonCancelar = Button(text="Salir", width=20, height=2)
        botonCancelar.pack(side=RIGHT, anchor=SE, padx=10, pady=5)
        
        botonRegPrestamo["command"] = self.regPrestamo
        
        botonRegCliente["command"] = self.regCliente
        botonConsultarCliente["command"] = self.consultarCliente
        botonEliminarCliente["command"] = self.eliminarCliente
        
        botonRegLibro["command"] = self.regLibro
        botonConsultarLibro["command"] = self.consultarLibro
        botonEliminarLibro["command"] = self.eliminarLibro
        
        botonReportes["command"] = self.reportes
        botonCancelar["command"] = self.cancelar
        
    def regPrestamo(self):
        #nuevaVentana = VentanaRegistrarPrestamo()
        #nuevaVentana.mostrar()
        pass
    
    def regCliente(self):
        nuevaVentana = VentanaAgregarSocio()
        nuevaVentana.mostrar()

    def consultarCliente(self):
        nuevaVentana = VentanaConsultarSocio()
        nuevaVentana.mostrar()

    def eliminarCliente(self):
        nuevaVentana = VentanaEliminarSocio()
        nuevaVentana.mostrar()
    
    def regLibro(self):
        nuevaVentana = VentanaAgregarLibro()
        nuevaVentana.mostrar()

    def consultarLibro(self):
        nuevaVentana = VentanaConsultarLibro()
        nuevaVentana.mostrar()

    def eliminarLibro(self):
        nuevaVentana = VentanaEliminarLibro()
        nuevaVentana.mostrar()
    
    def reportes(self):
        nuevaVentana = VentanaReportes()
        nuevaVentana.mostrar()

    def cancelar(self):
        self.ventana.destroy()
        
    def mostrar(self):
        self.ventana.mainloop()
        
VentanaMain().mostrar()
