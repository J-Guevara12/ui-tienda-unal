class Factura:
    def __init__(self):
        self.productos = []

    def añadirProducto(self,producto):
        self.productos.append(producto)

    def calcularTotal(self):
        count = 0
        for p in self.productos:
            count += p.existencias * p.precio
        return count

    def borrarProducto(self,i):
        self.productos.pop(i)
