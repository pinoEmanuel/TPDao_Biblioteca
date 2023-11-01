class Libro:
    
    def __init__(self, codigo, titulo, precioReposicion):
        self._codigo = codigo,
        self._titulo = titulo,
        self._precioReposicion = precioReposicion,
        self._estado = ["Disponible", "Prestado", "Extraviado"]
        
    