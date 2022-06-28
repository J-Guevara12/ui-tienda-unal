from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from src.models.OrdenDeCompra import OrdenDeCompra
from src.views.ordenCompra import OrdenCompra

from src.views.seleccionarProveedor import SeleccionarProveedor
from .Factura import Factura
from .Producto import Producto, ProductoInventario
from .Proveedor import Proveedor
from .Botones import BotonBorrar,BotonEditar
from ..views.facturacion import Facturacion
from ..views.productosProveedor import ProductosProveedor
from .ConexionDB import ConexionDB

conn = ConexionDB('https://backend-tienda-unal.herokuapp.com')

class Usuario:
    def __init__(self,usuario,nombre):
        self.id = usuario
        self.nombre = nombre

    def loadListaProductos(self,view):
        self.view = view

        view.table.setColumnWidth(0,180)
        view.table.setColumnWidth(1,500)
        view.table.setColumnWidth(2,280)
        view.table.setColumnWidth(3,157)
        view.table.setColumnWidth(4,157)

        view.botonAgregar.setVisible(False)
        view.botonVenta.setVisible(False)
        view.botonCompra.setVisible(False)
        view.botonProveedores.setVisible(False)
        view.botonCambios.setVisible(False)

class UsuarioAutorizado(Usuario):

    def loadListaProovedores(self,view):
        self.viewProveedores = view

        view.table.setColumnWidth(0,200)
        view.table.setColumnWidth(1,350)
        view.table.setColumnWidth(2,450)
        view.table.setColumnWidth(3,450)
        view.table.setColumnWidth(4,250)
        view.table.setColumnWidth(5,157)
        view.table.setColumnWidth(6,157)


        proveedores = list(map(lambda reg: Proveedor(*reg),conn.get('/proveedores/')))
        view.table.setRowCount(len(proveedores))
        
        for i,proveedor in enumerate(proveedores):
            proveedor.desplegarFila(i,view.table)
            botonBorrar = BotonBorrar(proveedor,self)
            botonEditar = BotonEditar(proveedor,self)
            view.table.setCellWidget(i,5,botonEditar)
            view.table.setCellWidget(i,6,botonBorrar)

    def agregarProveedor(self,proveedor):
        data = {
            'responsable': self.id, 
            'empresa': proveedor.empresa, 
            'contacto': proveedor.contacto,
            'email': proveedor.email,
            'telefono': proveedor.telefono
        }
        conn.post(f'/proveedor/{proveedor.nit}/',data)
        self.loadListaProovedores(self.viewProveedores)

    def editarProveedor(self,proveedor,nit):
        data = {
            'responsable': self.id, 
            'nit': proveedor.nit,
            'empresa': proveedor.empresa, 
            'contacto': proveedor.contacto,
            'email': proveedor.email,
            'telefono': proveedor.telefono
        }
        conn.put(f'/proveedor/{nit}/',data)
        self.loadListaProovedores(self.viewProveedores)

    def borrarProveedor(self,proveedor):
        data = {
            'responsable': self.id, 
            'empresa': proveedor.empresa, 
            'contacto': proveedor.contacto,
            'email': proveedor.email,
            'telefono': proveedor.telefono
        }
        conn.delete(f'/proveedor/{proveedor.nit}/',data)
        self.loadListaProovedores(self.viewProveedores)

    def cargarProductosProveedor(self,proveedor):
        self.dialog = QDialog()
        self.vistaProductoProveedor = ProductosProveedor()
        self.vistaProductoProveedor.setupUi(self.dialog,self,proveedor)
        self.dialog.show()

    def consultarSedes(self):
        return conn.get('/sedes/')

    def consultarExistenciasProducto(self,producto,sede):
        return conn.get(f'/inventario/{producto}/{sede}')

    def consultarProductosProveedor(self,proveedor):
        return list(map(lambda reg: Producto(*reg),conn.get(f'/productos-proveedor/{proveedor.nit}')))


    def consultarTodosLosProductos(self):
        res = conn.get('/productos/0')
        return list(map(lambda reg: Producto(*reg),res))

    def agregarProductoAProveedor(self,producto,proveedor):
        data = {'id': producto.id, 'responsable': self.id}
        conn.post(f'/productos-proveedor/{proveedor.nit}/',data)
        self.vistaProductoProveedor.loadProductos()

    def eliminarProductoAProveedor(self,producto,proveedor):
        data = {'id': producto.id, 'responsable': self.id}
        conn.delete(f'/productos-proveedor/{proveedor.nit}/',data)
        self.vistaProductoProveedor.loadProductos()

    def confirmarAccion(self,contrasena):
        return conn.get(f'/iniciar-sesion/{self.id}/{contrasena}')['status']


class UsuarioSysAdmin(UsuarioAutorizado):
    def __init__(self,usuario,nombre):
        super().__init__(usuario,nombre)

    def loadListaProductos(self,view):
        super().loadListaProductos(view)

        view.infoUsuario.setText(f'{self.nombre}\nAdministrador del sistema')

        view.botonAgregar.setVisible(True)
        view.botonProveedores.setVisible(True)
        view.botonCambios.setVisible(True)


        productos = self.consultarTodosLosProductos()
        view.table.setRowCount(len(productos))
        
        for i,producto in enumerate(productos):
            producto.desplegarFila(i,view.table)
            botonBorrar = BotonBorrar(producto,self)
            botonEditar = BotonEditar(producto,self)
            view.table.setCellWidget(i,3,botonEditar)
            view.table.setCellWidget(i,4,botonBorrar)

    def loadRegistroAcciones(self,view):

        view.table.setColumnWidth(0,350)
        view.table.setColumnWidth(1,650)
        view.table.setColumnWidth(2,300)
        acciones = conn.get('/registro-acciones/')
        view.table.setRowCount(len(acciones))
        
        for i,accion in enumerate(acciones):
            for j in range(3):
                view.table.setItem(i,j,QTableWidgetItem(accion[j]))

    def agregarProducto(self,producto):
        data = {"nombre": producto.nombre,"precio": producto.precio,"responsable": self.id}
        conn.post(f'/producto/{producto.id}',data)
        self.loadListaProductos(self.view)

    def editarProducto(self,producto):
        data = {"nombre": producto.nombre,"precio": producto.precio,"responsable": self.id}
        conn.put(f'/producto/{producto.id}',data)
        self.loadListaProductos(self.view)

    def borrarProducto(self,producto):
        data = {"nombre": producto.nombre,"precio": producto.precio,"responsable": self.id}
        conn.delete(f'/producto/{producto.id}',data)
        self.loadListaProductos(self.view)
        
    def editarInventario(self,producto,sede,cantidad,minimo,existe):
        data = {"existencias": cantidad, "existencias_min": minimo, "existe": existe,"responsable": self.id}
        conn.post(f'/inventario/{producto.id}/{sede}/',data)
        self.loadListaProductos(self.view)


class UsuarioAdministrativo(UsuarioAutorizado):
    def __init__(self,usuario,nombre):
        super().__init__(usuario,nombre)
        res = conn.get(f'/sede-trabajo/{usuario}/')

        for reg in res:
            self.sede = reg[0]

    def loadListaProductos(self,view):
        super().loadListaProductos(view)

        view.infoUsuario.setText(f'{self.nombre}\nUsuario Administrativo')
        view.botonCompra.setVisible(True)
        view.botonProveedores.setVisible(True)
        view.table.setHorizontalHeaderItem(3,QTableWidgetItem('Existencias'))
        view.table.setHorizontalHeaderItem(4,QTableWidgetItem('Mínimo'))

        productos = list(map(lambda reg: ProductoInventario(*reg),conn.get(f'/productos/{self.sede}')))
        view.table.setRowCount(len(productos))

        for i,producto in enumerate(productos):
            producto.desplegarFila(i,view.table)

    def seleccionarProveedor(self):
        self.dialog = QDialog()
        self.vistaSeleccionar = SeleccionarProveedor()
        self.vistaSeleccionar.setupUi(self.dialog,self)
        self.dialog.show()

    def consultarProveedores(self):
        return list(map(lambda reg: Proveedor(*reg),conn.get('/proveedores/')))

    def generarOrdenDeCompra(self,proveedor):
        self.dialog = QDialog()
        self.ordenDeCompra = OrdenDeCompra()
        self.vistaOrdenDeCompra = OrdenCompra()
        self.vistaOrdenDeCompra.setupUi(self.dialog,self,proveedor)
        self.dialog.show()

    def confirmarCompra(self,proveedor):
        if(len(self.ordenDeCompra.productos)!=0):
            data = {
                "responsable": self.id,
                "sede": self.sede,
                "proveedor": proveedor.nit,
                "productos": [ {
                    "id": x.id,
                    "cantidad": x.existencias
                } for x in self.ordenDeCompra.productos ]
            }
            conn.post('/orden-de-compra/',data)
            self.loadListaProductos(self.view)
            self.ordenDeCompra.productos = []


class UsuarioVendedor(Usuario):
    def __init__(self,usuario,nombre):
        super().__init__(usuario,nombre)
        self.factura = Factura()
        res = conn.get(f'/sede-trabajo/{usuario}/')
        for reg in res:
            self.sede = reg[0]

    def loadListaProductos(self,view):
        super().loadListaProductos(view)

        view.infoUsuario.setText(f'{self.nombre}\nAsesor Comercial')
        view.table.setHorizontalHeaderItem(3,QTableWidgetItem('Existencias'))
        view.botonVenta.setVisible(True)

        view.table.setColumnCount(4)
        view.table.setColumnWidth(0,140)
        view.table.setColumnWidth(1,600)
        view.table.setColumnWidth(2,267)
        view.table.setColumnWidth(3,267)

        self.productos = list(map(lambda reg: ProductoInventario(*reg),conn.get(f'/productos/{self.sede}')))
        view.table.setRowCount(len(self.productos))

        for i,producto in enumerate(self.productos):
            producto.desplegarFila(i,view.table)

    def generarFactura(self):
        self.vistaFactura = Facturacion()
        self.dialog = QDialog()
        self.vistaFactura.setupUi(self.dialog,self)
        self.dialog.show()


    def confirmarVenta(self):
        if(len(self.factura.productos)!=0):
            data = {
                "responsable": self.id,
                "sede": self.sede,
                "productos": [ {
                    "id": x.id,
                    "cantidad": x.existencias
                } for x in self.factura.productos ]
            }
            conn.post('/facturar/',data)
            self.loadListaProductos(self.view)
            self.factura.productos = []

def crearUsuario(ID):
    classes = [UsuarioVendedor,UsuarioAdministrativo,UsuarioSysAdmin]
    nivel = 0
    nombre = ''
    info = conn.get(f'/usuario/{ID}')
    for reg in info:
        nivel = reg[0]
        nombre = reg[1]
    if(nombre!=''):
        return classes[nivel](ID,nombre)
