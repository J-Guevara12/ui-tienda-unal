from .ViewListaProductos import Ui_MainWindow

class ListaProductos(Ui_MainWindow):
    def setupUi(self,MainWindow):

        super().setupUi(MainWindow)

        self.MainWindow = MainWindow
        self.MainWindow.usuario.loadListaProductos(self)

        self.botonAgregar.clicked.connect(lambda: self.MainWindow.editarProducto.agregarProducto(self.MainWindow.usuario))
        self.botonProveedores.clicked.connect(lambda: self.MainWindow.listaProveedores.setupUi(self.MainWindow))
        self.botonCambios.clicked.connect(lambda: self.MainWindow.registroAcciones.setupUi(self.MainWindow))
        self.botonCerrarSesion.clicked.connect(lambda: self.cerrarSesion())
        self.botonVenta.clicked.connect(lambda: self.MainWindow.usuario.generarFactura())
        self.botonCompra.clicked.connect(lambda: self.MainWindow.usuario.seleccionarProveedor())

    def retranslateUi(self,MainWindow):
        super().retranslateUi(MainWindow)

    def cerrarSesion(self):
        self.MainWindow.loginWindow.setupUi(self.MainWindow)
        self.MainWindow.usuario = None
