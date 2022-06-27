from .ViewLogin import Ui_MainWindow
from PyQt5.QtCore import pyqtSlot 
from hashlib import sha256
from ..models.Usuarios import crearUsuario


class Login(Ui_MainWindow):
    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.cur = MainWindow.cur
        self.conexion = MainWindow.conexion
        self.loginButton.clicked.connect(lambda: self.iniciarSesion())

        #Erase this please
        #self.MainWindow.usuario =  crearUsuario(str(1002655778),self.cur,self.MainWindow.conexion)
        #self.MainWindow.listaProductos.setupUi(self.MainWindow)

    def retranslateUi(self,MainWindow):
        super().retranslateUi(MainWindow)

    @pyqtSlot()
    def iniciarSesion(self):
        h = sha256()
        h.update(self.contrasena.text().encode())
        consigna = f"SELECT ID FROM USUARIOS WHERE CONTRASEÑA='{h.hexdigest()}'"
        self.cur.execute(consigna)
        for register in self.cur:
            if(self.usuario.text()==str(register[0])):
                self.MainWindow.usuario =  crearUsuario(str(register[0]),self.cur,self.conexion)
                self.MainWindow.listaProductos.setupUi(self.MainWindow)
                return
        self.mensajeError.setText('Error, usuario o contraseña incorrectos')
