from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from src.models.Producto import Producto
from .ViewEditarProducto import Ui_Dialog
from .editarInventario import EditarInventario

class EditarProducto(Ui_Dialog):
    def setupUi(self,Dialog):
        super().setupUi(Dialog)
        self.window = Dialog
        self.cancelar.clicked.connect(lambda: self.window.close())
        self.inventario.clicked.connect(lambda: self.cambiarDialogo())

    def retranslateUi(self,Dialog):
        super().retranslateUi(Dialog)

    def agregarProducto(self,user):
        self.editable = True
        self.user = user
        self.IDLabel.setText('')
        self.inputNombre.setText('')
        self.inputPrecio.setText('')
        self.inventario.setVisible(False)
        self.confirmar.clicked.connect(lambda: self.crearProducto())
        self.window.exec_()

    def editarProducto(self,producto,user):
        self.producto = producto
        self.user = user
        self.IDProducto = producto.id
        self.IDLabel.setText(f'ID: {producto.id}')
        self.inputNombre.setText(producto.nombre)
        self.inputPrecio.setText(str(producto.precio))
        self.inventario.setVisible(True)
        self.confirmar.clicked.connect(lambda: self.editarProductoConfirmado())
        self.window.show()

    @pyqtSlot()
    def crearProducto(self):
        if self.editable:
            producto = Producto(0,self.inputNombre.text(),self.inputPrecio.text())
            self.user.agregarProducto(producto)
            self.window.close()
            self.editable = False

    @pyqtSlot()
    def editarProductoConfirmado(self):
        producto = Producto(self.IDProducto,self.inputNombre.text(),self.inputPrecio.text())
        self.user.editarProducto(producto)
        self.window.close()

    @pyqtSlot(bool)
    def cambiarDialogo(self):
        listaSedes = self.user.consultarSedes()
        self.dialog2 = QDialog()
        self.editarInventario = EditarInventario()
        self.editarInventario.setupUi(self.dialog2,listaSedes,self.user)
        self.window.close()
        self.editarInventario.editarInventario(self.producto)
