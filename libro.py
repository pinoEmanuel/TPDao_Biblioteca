class Libro:
    
    def __init__(self, titulo, precioReposicion):
        
        self._titulo = titulo
        self._precioReposicion = precioReposicion
        self.estado = ["Disponible", "Prestado", "Extraviado"]
        