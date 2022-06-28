from .ViewLogin import Ui_MainWindow
from PyQt5.QtCore import pyqtSlot 
from hashlib import sha256
from ..models.Usuarios import crearUsuario
from ..models.ConexionDB import ConexionDB


class Login(Ui_MainWindow):
    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.cur = MainWindow.cur
        self.conexion = MainWindow.conexion
        self.loginButton.clicked.connect(lambda: self.iniciarSesion())

        #Erase this please
        self.MainWindow.usuario =  crearUsuario(str(1002655780),self.cur,self.MainWindow.conexion)
        self.MainWindow.listaProductos.setupUi(self.MainWindow)

    def retranslateUi(self,MainWindow):
        super().retranslateUi(MainWindow)

    @pyqtSlot()
    def iniciarSesion(self):
        h = sha256()
        h.update(self.contrasena.text().encode())
        #conn = ConexionDB('http://127.0.0.1:5000')
        conn = ConexionDB('https://backend-tienda-unal.herokuapp.com')
        data = {'usuario': str(self.usuario.text()),'contrasena': str(h.hexdigest())}
        res = conn.get(f'/iniciar-sesion/{data["usuario"]}/{data["contrasena"]}')
        if res['status']:
            self.MainWindow.usuario =  crearUsuario(self.usuario.text(),self.cur,self.conexion)
            self.MainWindow.listaProductos.setupUi(self.MainWindow)
            return
        else:
            self.mensajeError.setText('Error, usuario o contraseña incorrectos')
