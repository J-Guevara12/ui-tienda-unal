class OrdenDeCompra:
    def __init__(self):
        self.productos = []

    def añadirProducto(self,producto):
        self.productos.append(producto)

    def borrarProducto(self,i):
        self.productos.pop(i)
