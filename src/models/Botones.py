from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QPushButton
from ..views.confirmarOperacion import ConfirmarOperacion
from .Producto import Producto
from .Proveedor import Proveedor

class BotonEditar(QPushButton):
    def __init__(self,objeto,usuario):
        super(BotonEditar,self).__init__()
        self.objeto = objeto
        self.usuario = usuario
        self.clicked.connect(lambda: self.editar())
        self.setStyleSheet("""
                    QPushButton {
                        background-color: #e3fff9;
                        border-radius: 0;
                    }
                    QPushButton:hover {
                        background-color: #f0ffff;
                    }""")

    @pyqtSlot()
    def editar(self):
        if(isinstance(self.objeto,Producto)):
            self.usuario.view.MainWindow.editarProducto.editarProducto(self.objeto,self.usuario)
        elif(isinstance(self.objeto,Proveedor)):
            self.usuario.view.MainWindow.editarProveedor.editarProveedor(self.objeto,self.usuario)

class BotonBorrar(QPushButton):
    def __init__(self,objeto,usuario):
        super(BotonBorrar,self).__init__()
        self.objeto = objeto
        self.usuario = usuario
        self.setStyleSheet("""
                    QPushButton {
                        background-color: #ffe3e3;
                        border-radius: 0;
                    }
                    QPushButton:hover {
                        background-color: #ffefe9;
                    }""")
        self.clicked.connect(lambda: self.confirmarOperacion())

    def confirmarOperacion(self):
            self.ventana = QDialog()
            self.confirmar = ConfirmarOperacion()
            self.confirmar.setupUi(self.ventana)
            self.confirmar.confirmarBorrado(self.usuario,self.objeto)
