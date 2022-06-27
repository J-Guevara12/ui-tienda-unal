from .ViewAgregarProducto import Ui_Dialog
from ..models.Producto import ProductoInventario

class AgregarProducto(Ui_Dialog):

    def setupUiVenta(self,Dialog,usuario,proveedor):
        self.usuario = usuario
        self.proveedor = proveedor
        self.dialog = Dialog

        super().setupUi(Dialog)

        self.loadProductosCompra()
        self.selectProducto.setCurrentIndex(0)
        self.cambiarProducto()

        self.inputNombre.textEdited.connect(lambda: self.loadProductosCompra())
        self.cancelar.clicked.connect(lambda: Dialog.close())
        self.selectProducto.currentIndexChanged.connect(lambda: self.cambiarProducto())
        self.confirmar.clicked.connect(lambda: self.guardarProductoCompra())

    def setupUi(self,Dialog,usuario):
        self.usuario = usuario
        self.dialog = Dialog

        super().setupUi(Dialog)

        self.loadProductos()
        self.selectProducto.setCurrentIndex(0)
        self.cambiarProducto()

        self.inputNombre.textEdited.connect(lambda: self.loadProductos())
        self.cancelar.clicked.connect(lambda: Dialog.close())
        self.selectProducto.currentIndexChanged.connect(lambda: self.cambiarProducto())
        self.confirmar.clicked.connect(lambda: self.guardarProducto())

    def retranslateUi(self,Dialog):
        super().retranslateUi(Dialog)

    def loadProductos(self):
        self.listaProductos = list(filter(lambda x: compareStrings(self.inputNombre.text(),x.nombre),self.usuario.productos))
        self.listaProductos = list(filter(lambda x: noRepetir(x,self.usuario.factura.productos),self.listaProductos))
        self.selectProducto.clear()
        for producto in self.listaProductos:
            self.selectProducto.addItem(f'{producto.id}. {producto.nombre}')

    def loadProductosCompra(self):
        self.listaProductos = list(filter(lambda x: compareStrings(self.inputNombre.text(),x.nombre),self.usuario.consultarProductosProveedor(self.proveedor)))
        self.listaProductos = list(filter(lambda x: noRepetir(x,self.usuario.ordenDeCompra.productos),self.listaProductos))
        self.selectProducto.clear()
        for producto in self.listaProductos:
            self.selectProducto.addItem(f'{producto.id}. {producto.nombre}')

    def cambiarProducto(self):
        index = self.selectProducto.currentIndex()
        if(index!=-1):
            self.p = self.listaProductos[index]

    def guardarProducto(self):
        if(self.inputCantidad.text()!=''):
            if(self.inputCantidad.text()!='0' and int(self.inputCantidad.text())<self.p.existencias):
                self.productoSeleccionado = ProductoInventario(self.p.id,self.p.nombre,self.p.precio,int(self.inputCantidad.text()),0)
                self.usuario.factura.añadirProducto(self.productoSeleccionado)
                self.usuario.vistaFactura.loadProductosFactura()
                self.dialog.close()

    def guardarProductoCompra(self):
        if(self.inputCantidad.text()!=''):
            if(self.inputCantidad.text()!='0'):
                self.productoSeleccionado = ProductoInventario(self.p.id,self.p.nombre,self.p.precio,int(self.inputCantidad.text()),0)
                self.usuario.ordenDeCompra.añadirProducto(self.productoSeleccionado)
                self.usuario.vistaOrdenDeCompra.loadProductos()
                self.dialog.close()


def compareStrings(s1,s2):
    for i,s in enumerate(s1):
        if(s.lower()!=s2[i].lower()):
            return False

    return True

def noRepetir(p,lProductos):
    for i in lProductos:
        if(p.id==i.id):
            return False
    return True
