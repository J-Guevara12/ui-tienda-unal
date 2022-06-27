from PyQt5.QtCore import pyqtSlot

from src.models.Producto import Producto
from .ViewEditarInventario import Ui_Dialog

class EditarInventario(Ui_Dialog):
    def setupUi(self,Dialog,listaSedes,usuario):
        self.usuario = usuario
        super().setupUi(Dialog)
        self.window = Dialog
        for sede in listaSedes:
            self.selectSede.addItem(*sede)
        self.cancelar.clicked.connect(lambda: self.window.close())
        self.confirmar.clicked.connect(lambda: self.confirmarEdicion())

    def retranslateUi(self,Dialog):
        super().retranslateUi(Dialog)

    def editarInventario(self,producto):
        self.producto = producto
        self.inputCantidad.setText('')
        self.inputMinimo.setText('')
        self.confirmar.clicked.connect(lambda: self.window.close())
        self.consultarInventario()
        self.selectSede.currentIndexChanged.connect(lambda: self.consultarInventario())
        self.window.show()

    def consultarInventario(self):
        data = self.usuario.consultarExistenciasProducto(self.producto.id,self.selectSede.currentData())
        if(len(data)!=0):
            self.inputCantidad.setText(str(data[0][0]))
            self.inputMinimo.setText(str(data[0][1]))
            self.existeInventario = True
        else:
            self.inputCantidad.setText('0')
            self.inputMinimo.setText('0')
            self.existeInventario = False

    def confirmarEdicion(self):
        self.usuario.editarInventario(self.producto,self.selectSede.currentData(),self.inputCantidad.text(),self.inputMinimo.text(),self.existeInventario)
