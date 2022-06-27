from .ViewAgregarProducto import Ui_Dialog
from ..models.Producto import Producto

class AgregarProductoProveedor(Ui_Dialog):
    def setupUi(self,Dialog,usuario,proveedor):
        self.usuario = usuario
        self.proveedor = proveedor
        self.dialog = Dialog

        super().setupUi(Dialog)

        self.label.setVisible(False)
        self.inputCantidad.setVisible(False)

        self.loadProductos()
        self.selectProducto.setCurrentIndex(0)
        self.cambiarProducto()

        self.inputNombre.textEdited.connect(lambda: self.loadProductos())
        self.selectProducto.currentIndexChanged.connect(lambda: self.cambiarProducto())
        self.confirmar.clicked.connect(lambda: self.guardarProducto())
        self.cancelar.clicked.connect(lambda: Dialog.close())

    def retranslateUi(self,Dialog):
        super().retranslateUi(Dialog)

    def loadProductos(self):
        self.productos = self.usuario.consultarTodosLosProductos()
        productosDisponibles = self.usuario.consultarProductosProveedor(self.proveedor)
        self.listaProductos = list(filter(lambda x: compareStrings(self.inputNombre.text(),x.nombre),self.productos))
        self.listaProductos = list(filter(lambda x: noRepetir(x,productosDisponibles),self.listaProductos))
        self.selectProducto.clear()
        for producto in self.listaProductos:
            self.selectProducto.addItem(f'{producto.id}. {producto.nombre}')

    def cambiarProducto(self):
        index = self.selectProducto.currentIndex()
        if(index!=-1):
            self.p = self.listaProductos[index]

    def guardarProducto(self):
        self.productoSeleccionado = Producto(self.p.id,self.p.nombre,self.p.precio)
        self.usuario.agregarProductoAProveedor(self.productoSeleccionado,self.proveedor)
        self.usuario.vistaProductoProveedor.loadProductos()
        self.dialog.close()


def compareStrings(s1,s2):
    for i,s in enumerate(s1):
        if(s.lower()!=s2[i].lower()):
            return False

    return True

def noRepetir(p,lProductos):
    for i in lProductos:
        if(p.id==i.id):
            return False
    return True
