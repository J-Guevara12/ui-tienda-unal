from .ViewRegistroAcciones import Ui_MainWindow

class RegistroAcciones(Ui_MainWindow):
    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        self.usuario = MainWindow.usuario
        self.usuario.loadRegistroAcciones(self)
        self.botonProductos.clicked.connect(lambda: MainWindow.listaProductos.setupUi(MainWindow))

    def retranslateUi(self,Dialog):
        super().retranslateUi(Dialog)
