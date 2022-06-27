from .ViewSeleccionarProveedor import Ui_Dialog

class SeleccionarProveedor(Ui_Dialog):
    def setupUi(self,Dialog,usuario):
        self.usuario = usuario
        self.dialog = Dialog

        super().setupUi(Dialog)

        self.loadProveedores()

        self.selectProveedor.currentIndexChanged.connect(self.seleccionarProveedor)

    def retranslateUi(self,Dialog):
        super().retranslateUi(Dialog)

    def loadProveedores(self):
        self.proveedores = self.usuario.consultarProveedores()
        self.selectProveedor.clear()
        self.selectProveedor.addItem('')
        for proveedor in self.proveedores:
            self.selectProveedor.addItem(proveedor.empresa,proveedor)

    def seleccionarProveedor(self):
        self.usuario.generarOrdenDeCompra(self.selectProveedor.currentData())
        self.dialog.close()
