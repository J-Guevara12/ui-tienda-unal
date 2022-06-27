from PyQt5.QtWidgets import QDialog, QPushButton
from .ViewFacturacion import Ui_Dialog
from .agregarProducto import AgregarProducto

class Facturacion(Ui_Dialog):
    def setupUi(self,Dialog,usuario):
        self.dialog = Dialog
        self.usuario = usuario
        super().setupUi(Dialog)

        self.infoResponsable.setText(f'Responsable: {usuario.nombre}')
        self.cancelar.clicked.connect(self.cancelarVenta)
        self.confirmar.clicked.connect(self.confirmarVenta)

        self.table.setColumnWidth(0,70)
        self.table.setColumnWidth(1,270)
        self.table.setColumnWidth(2,100)
        self.table.setColumnWidth(3,120)
        self.table.setColumnWidth(4,120)
        self.loadProductosFactura()

        self.botonAgregar.clicked.connect(self.agregarProducto)

    def retranslateUi(self,Dialog):
        self.dialog = Dialog
        super().retranslateUi(Dialog)

    def agregarProducto(self):
        self.window = QDialog()
        self.ventanaAgregar = AgregarProducto()
        self.ventanaAgregar.setupUi(self.window,self.usuario)
        self.window.show()

    def loadProductosFactura(self):
        self.table.setRowCount(len(self.usuario.factura.productos))
        for i, producto in enumerate(self.usuario.factura.productos):
            btn = BotonBorrar(i,self.usuario,self)
            producto.desplegarFila(i,self.table)
            self.table.setCellWidget(i,4,btn)
        
        self.infoTotal.setText(f'Total: {self.usuario.factura.calcularTotal()}')

    def confirmarVenta(self):
        self.usuario.confirmarVenta()
        self.dialog.close()

    def cancelarVenta(self):
        self.usuario.factura.productos = []
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
        self.usuario.factura.borrarProducto(self.index)
        self.vista.loadProductosFactura()
