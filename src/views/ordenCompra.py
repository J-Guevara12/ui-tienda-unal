from PyQt5.QtWidgets import QDialog, QPushButton
from .ViewOrdenCompra import Ui_Dialog
from .agregarProducto import AgregarProducto

class OrdenCompra(Ui_Dialog):
    def setupUi(self,Dialog,usuario,proveedor):
        self.dialog = Dialog
        self.usuario = usuario
        self.proveedor = proveedor
        super().setupUi(Dialog)

        self.infoResponsable.setText(f'Empresa: {proveedor.empresa}\nResponsable: {usuario.nombre}')
        self.cancelar.clicked.connect(self.cancelarCompra)
        self.confirmar.clicked.connect(self.confirmarVenta)

        self.table.setColumnWidth(0,90)
        self.table.setColumnWidth(1,310)
        self.table.setColumnWidth(2,148)
        self.table.setColumnWidth(3,150)

        self.loadProductos()

        self.botonAgregar.clicked.connect(self.agregarProducto)

    def retranslateUi(self,Dialog):
        self.dialog = Dialog
        super().retranslateUi(Dialog)

    def agregarProducto(self):
        self.window = QDialog()
        self.ventanaAgregar = AgregarProducto()
        self.ventanaAgregar.setupUiVenta(self.window,self.usuario,self.proveedor)
        self.window.show()

    def loadProductos(self):
        self.table.setRowCount(len(self.usuario.ordenDeCompra.productos))
        for i, producto in enumerate(self.usuario.ordenDeCompra.productos):
            btn = BotonBorrar(i,self.usuario,self)
            producto.desplegarFilaCompra(i,self.table)
            self.table.setCellWidget(i,3,btn)
        
    def confirmarVenta(self):
        self.usuario.confirmarCompra(self.proveedor)
        self.dialog.close()

    def cancelarCompra(self):
        self.usuario.ordenDeCompra.productos = []
        self.dialog.close()
            

class BotonBorrar(QPushButton):
    def __init__(self,index,usuario,vista):
        self.index = index
        self.usuario = usuario
        self.vista = vista

        super(BotonBorrar,self).__init__()

        self.setStyleSheet("""
                    QPushButton {
                        background-color: #ffe3e3;
                        border-radius: 0;
                    }
                    QPushButton:hover {
                        background-color: #ffefe9;
                    }""")

        self.clicked.connect(self.borrarProducto)

    def borrarProducto(self):
        self.usuario.ordenDeCompra.borrarProducto(self.index)
        self.vista.loadProductos()
