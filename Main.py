import sys
import sqlite3
from PyQt5.QtWidgets import QMainWindow,QApplication, QDialog

from src.views.login import Login
from src.views.listaProductos import ListaProductos
from src.views.editarProducto import EditarProducto
from src.views.editarProveedor import EditarProveedor
from src.views.listaProveedores import ListaProveedores
from src.views.registroAcciones import RegistroAcciones

conexion = sqlite3.connect('./database.db')
cur = conexion.cursor()

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.dialog = QDialog()
        self.dialog2 = QDialog()
        self.conexion = conexion
        self.cur = cur
        self.usuario = None
        self.loginWindow = Login()
        self.listaProductos = ListaProductos()
        self.listaProveedores = ListaProveedores()
        self.registroAcciones = RegistroAcciones()
        self.editarProducto = EditarProducto()
        self.editarProveedor = EditarProveedor()
        self.editarProducto.setupUi(self.dialog)
        self.editarProveedor.setupUi(self.dialog2)
        self.loginWindow.setupUi(self)
        self.show()

app = QApplication(sys.argv)
window = VentanaPrincipal()
sys.exit(app.exec_())
 
