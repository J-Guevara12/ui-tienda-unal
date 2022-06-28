from hashlib import sha256

from src.models.Proveedor import Proveedor
from src.models.Producto import Producto
from .ViewConfirmarOperacion import Ui_Dialog

class ConfirmarOperacion(Ui_Dialog):
    def setupUi(self,Dialog):
        super().setupUi(Dialog)
        self.window = Dialog
        self.cancelar.clicked.connect(lambda: self.window.close())

    def retranslateUi(self,Dialog):
        super().retranslateUi(Dialog)

    def confirmarBorrado(self,usuario,objeto):
        self.window.show()
        self.usuario = usuario
        if(isinstance(objeto,Producto)):
            self.confirmar.clicked.connect(lambda: self.confirmarAccion(lambda: self.usuario.borrarProducto(objeto)))
        elif(isinstance(objeto,Proveedor)):
            self.confirmar.clicked.connect(lambda: self.confirmarAccion(lambda: self.usuario.borrarProveedor(objeto)))


    def confirmarAccion(self,accion):
        h = sha256()
        h.update(self.contrasena.text().encode())
        if(self.usuario.confirmarAccion(h.hexdigest())):
            accion()
            self.window.close()
            return
        else:
            self.mensajeError.setText('contraseña incorrecta')
