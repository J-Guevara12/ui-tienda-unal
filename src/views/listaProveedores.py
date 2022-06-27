from .ViewListaProveedores import Ui_MainWindow

class ListaProveedores(Ui_MainWindow):
    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.botonAgregar.clicked.connect(lambda: self.MainWindow.editarProveedor.agregarProveedor(self.MainWindow.usuario))
        self.MainWindow.usuario.loadListaProovedores(self)
        self.botonProductos.clicked.connect(lambda: self.MainWindow.listaProductos.setupUi(self.MainWindow))

    def retranslateUi(self,MainWindow):
        super().retranslateUi(MainWindow)
