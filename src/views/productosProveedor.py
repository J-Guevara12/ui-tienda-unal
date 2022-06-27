from PyQt5.QtWidgets import QDialog, QPushButton

from src.views.agregarProductoProveedor import AgregarProductoProveedor
from .ViewProductosProveedor import Ui_Dialog 

class ProductosProveedor(Ui_Dialog):
    def setupUi(self,Dialog,usuario,proveedor):
        self.usuario = usuario
        self.proveedor = proveedor
        super().setupUi(Dialog)

        self.table.setColumnWidth(1,232)
        self.table.setColumnWidth(2,157)

        self.loadProductos()

        self.botonAgregar.clicked.connect(self.agregarProducto)
        self.cancelar.clicked.connect(Dialog.close)

    def retranslateUi(self,Dialog):
        super().retranslateUi(Dialog)

    def agregarProducto(self):
        self.dialogo2 = QDialog()
        self.vistaAgregarProducto = AgregarProductoProveedor()
        self.vistaAgregarProducto.setupUi(self.dialogo2,self.usuario,self.proveedor)
        self.dialogo2.show()

    def loadProductos(self):
        self.productos = self.usuario.consultarProductosProveedor(self.proveedor)
        self.table.setRowCount(len(self.productos))
        for i, producto in enumerate(self.productos):
            producto.desplegarFila(i,self.table)
            btn = BotonBorrar(producto,self.proveedor,self.usuario)
            self.table.setCellWidget(i,2,btn)
        
class BotonBorrar(QPushButton):
    def __init__(self,producto,proveedor,usuario):
        super(BotonBorrar,self).__init__()
        self.producto = producto
        self.proveedor = proveedor
        self.usuario = usuario
        self.setStyleSheet("""
                    QPushButton {
                        background-color: #ffe3e3;
                        border-radius: 0;
                    }
                    QPushButton:hover {
                        background-color: #ffefe9;
                    }""")
        self.clicked.connect(lambda: self.usuario.eliminarProductoAProveedor(self.producto,self.proveedor))
