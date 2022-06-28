from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from ..models.Proveedor import Proveedor
from .ViewEditarProveedor import Ui_Dialog

class EditarProveedor(Ui_Dialog):
    def setupUi(self,Dialog):
        super().setupUi(Dialog)
        self.window = Dialog
        self.cancelar.clicked.connect(lambda: self.window.close())
        self.editarProductos.clicked.connect(lambda: self.cambiarDialogo())

    def retranslateUi(self,Dialog):
        super().retranslateUi(Dialog)

    def agregarProveedor(self,user):
        self.editable = True
        self.usuario = user
        self.IDLabel.setText('')
        self.inputNit.setText('')
        self.inputEmpresa.setText('')
        self.inputNombre.setText('')
        self.inputEmail.setText('')
        self.inputTelefono.setText('')
        self.editarProductos.setVisible(False)
        self.confirmar.clicked.connect(lambda: self.crearProveedor())
        self.window.exec_()

    def editarProveedor(self,proveedor,usuario):
        self.proveedor = proveedor
        self.usuario = usuario
        self.IDLabel.setText(f'{proveedor.empresa}')
        self.inputNit.setText(str(proveedor.nit))
        self.inputEmpresa.setText(proveedor.empresa)
        self.inputNombre.setText(proveedor.contacto)
        self.inputEmail.setText(proveedor.email)
        self.inputTelefono.setText(str(proveedor.telefono))
        self.editarProductos.setVisible(True)
        self.confirmar.clicked.connect(lambda: self.editarProveedorConfirmado())
        self.window.show()

    @pyqtSlot()
    def crearProveedor(self):
        if self.editable:
            proveedor = Proveedor(self.inputNit.text(),self.inputEmpresa.text(),self.inputNombre.text(),self.inputEmail.text(),self.inputTelefono.text())
            self.usuario.agregarProveedor(proveedor)
            self.window.close()
            self.editable = False

    @pyqtSlot()
    def editarProveedorConfirmado(self):
        proveedor = Proveedor(self.inputNit.text(),self.inputEmpresa.text(),self.inputNombre.text(),self.inputEmail.text(),self.inputTelefono.text())
        self.usuario.editarProveedor(proveedor,self.proveedor.nit)
        self.window.close()

    @pyqtSlot(bool)
    def cambiarDialogo(self):
        self.usuario.cargarProductosProveedor(self.proveedor)
