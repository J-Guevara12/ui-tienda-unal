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

class Usuario:
    def __init__(self,usuario,nombre,cur,conexion):
        self.id = usuario
        self.nombre = nombre
        self.cur = cur
        self.conexion = conexion

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

        self.cur.execute('SELECT * FROM PROVEEDORES')

        proveedores = list(map(lambda reg: Proveedor(*reg),self.cur.fetchall()))
        view.table.setRowCount(len(proveedores))
        
        for i,proveedor in enumerate(proveedores):
            proveedor.desplegarFila(i,view.table)
            botonBorrar = BotonBorrar(proveedor,self)
            botonEditar = BotonEditar(proveedor,self)
            view.table.setCellWidget(i,5,botonEditar)
            view.table.setCellWidget(i,6,botonBorrar)

    def registrarAccion(self,accion):
        self.cur.execute(f"INSERT INTO REGISTROS_MODIFICACIONES (RESPONSABLE,CAMBIO,FECHA) VALUES ({self.id},'{accion}',datetime('now'))")

    def agregarProveedor(self,proveedor):
        self.registrarAccion(f'AÑADIÓ Proveedor {proveedor.empresa}')
        self.cur.execute(f"INSERT INTO PROVEEDORES (NIT, NOMBRE_EMPRESA, NOMBRE_CONTACTO,EMAIL_CONTACTO,TELEFONO) VALUES ({proveedor.nit},'{proveedor.empresa}','{proveedor.contacto}','{proveedor.email}',{proveedor.telefono})")
        self.conexion.commit()
        self.loadListaProovedores(self.viewProveedores)

    def editarProveedor(self,proveedor):
        self.registrarAccion(f'EDITÓ proveedor {proveedor.empresa}')
        self.cur.execute(f"""UPDATE PROVEEDORES
                            SET NIT={proveedor.nit}, NOMBRE_EMPRESA = '{proveedor.empresa}', NOMBRE_CONTACTO = '{proveedor.contacto}', 
                            EMAIL_CONTACTO = '{proveedor.email}', TELEFONO = {proveedor.telefono}
                            WHERE NIT = {proveedor.nit}
                         """)
        self.conexion.commit()
        self.loadListaProovedores(self.viewProveedores)

    def borrarProveedor(self,proveedor):
        self.registrarAccion(f'BORRÓ proveedor {proveedor.empresa}')
        self.cur.execute(f"""
                         DELETE FROM PROVEEDORES WHERE NIT={proveedor.nit}
                         """)
        self.conexion.commit()
        self.loadListaProovedores(self.viewProveedores)

    def cargarProductosProveedor(self,proveedor):
        self.dialog = QDialog()
        self.vistaProductoProveedor = ProductosProveedor()
        self.vistaProductoProveedor.setupUi(self.dialog,self,proveedor)
        self.dialog.show()

    def consultarSedes(self):
        self.cur.execute('SELECT UBICACION, ID_ALMACEN FROM ALMACEN')
        return self.cur.fetchall()

    def consultarExistenciasProducto(self,producto,sede):
        self.cur.execute(f"""SELECT EXISTENCIAS, EXISTENCIAS_MIN FROM INVENTARIO 
                                    WHERE ID_PRODUCTO = {producto} AND ID_ALMACEN={sede}""")
        return self.cur.fetchall()

    def consultarProductosProveedor(self,proveedor):
        self.cur.execute(f"""SELECT PRODUCTOS.ID_PRODUCTO, NOMBRE, PRECIO FROM PRODUCTOS  
                         INNER JOIN PRODUCTOS_PROVEEDOR ON PRODUCTOS.ID_PRODUCTO = PRODUCTOS_PROVEEDOR.ID_PRODUCTO 
                         WHERE PRODUCTOS_PROVEEDOR.ID_PROVEEDOR = {proveedor.nit}""")
        return list(map(lambda reg: Producto(*reg),self.cur.fetchall()))


    def consultarTodosLosProductos(self):
        self.cur.execute('SELECT * FROM PRODUCTOS')
        return list(map(lambda reg: Producto(*reg),self.cur.fetchall()))

    def agregarProductoAProveedor(self,producto,proveedor):
        self.registrarAccion(f'AÑADIÓ producto {producto.id} A proveedor {proveedor.nit}')
        self.cur.execute(f"""INSERT INTO PRODUCTOS_PROVEEDOR (ID_PRODUCTO,ID_PROVEEDOR) VALUES ({producto.id}, {proveedor.nit})""")
        self.conexion.commit()

    def eliminarProductoAProveedor(self,producto,proveedor):
        self.registrarAccion(f'AÑADIÓ producto {producto.id} A proveedor {proveedor.nit}')
        self.cur.execute(f"""DELETE FROM PRODUCTOS_PROVEEDOR WHERE ID_PRODUCTO={producto.id} AND ID_PROVEEDOR = {proveedor.nit}""")
        self.conexion.commit()
        self.vistaProductoProveedor.loadProductos()


class UsuarioSysAdmin(UsuarioAutorizado):
    def __init__(self,usuario,nombre,cur,conexion):
        super().__init__(usuario,nombre,cur,conexion)

    def loadListaProductos(self,view):
        super().loadListaProductos(view)

        view.infoUsuario.setText(f'{self.nombre}\nAdministrador del sistema')

        view.botonAgregar.setVisible(True)
        view.botonProveedores.setVisible(True)
        view.botonCambios.setVisible(True)

        self.cur.execute('SELECT * FROM PRODUCTOS')

        productos = list(map(lambda reg: Producto(*reg),self.cur.fetchall()))
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
        self.cur.execute("""SELECT USUARIOS.NOMBRE, CAMBIO, FECHA 
                            FROM REGISTROS_MODIFICACIONES INNER JOIN USUARIOS ON 
                            USUARIOS.ID = REGISTROS_MODIFICACIONES.RESPONSABLE""")
        acciones = self.cur.fetchall()
        view.table.setRowCount(len(acciones))
        
        for i,accion in enumerate(acciones):
            for j in range(3):
                view.table.setItem(i,j,QTableWidgetItem(accion[j]))

    def agregarProducto(self,producto):
        self.registrarAccion(f'AÑADIÓ producto {producto.nombre}')
        self.cur.execute(f"INSERT INTO PRODUCTOS (NOMBRE,PRECIO) VALUES ('{producto.nombre}','{producto.precio}')")
        self.conexion.commit()
        self.loadListaProductos(self.view)

    def editarProducto(self,producto):
        self.registrarAccion(f'EDITÓ producto {producto.id}')
        self.cur.execute(f"""UPDATE PRODUCTOS
                            SET NOMBRE='{producto.nombre}', precio={producto.precio}
                            WHERE ID_PRODUCTO = {producto.id}
                         """)
        self.conexion.commit()
        self.loadListaProductos(self.view)

    def borrarProducto(self,producto):
        self.registrarAccion(f'BORRÓ producto {producto.id}')
        self.cur.execute(f"""
                         DELETE FROM PRODUCTOS WHERE ID_PRODUCTO={producto.id}
                         """)
        self.conexion.commit()
        self.loadListaProductos(self.view)

    def editarInventario(self,producto,sede,cantidad,minimo,existe):
        self.registrarAccion(f'EDITÓ las existencías producto {producto.id} en la sede {sede}')
        if existe:
            self.cur.execute(f"""UPDATE INVENTARIO
                                SET EXISTENCIAS='{cantidad}', EXISTENCIAS_MIN={minimo}
                                WHERE ID_PRODUCTO = {producto.id} and ID_ALMACEN={sede}
                             """)
        else: 
            self.cur.execute(f"INSERT INTO INVENTARIO VALUES ({producto.id},{sede},{cantidad},{minimo})")

        self.conexion.commit()
        self.loadListaProductos(self.view)


class UsuarioAdministrativo(UsuarioAutorizado):
    def __init__(self,usuario,nombre,cur,conexion):
        super().__init__(usuario,nombre,cur,conexion)
        self.cur.execute(f'SELECT SEDE_TRABAJO FROM USUARIOS WHERE ID={self.id}')

        for reg in self.cur:
            self.sede = reg[0]

    def loadListaProductos(self,view):
        super().loadListaProductos(view)

        view.infoUsuario.setText(f'{self.nombre}\nUsuario Administrativo')
        view.botonCompra.setVisible(True)
        view.botonProveedores.setVisible(True)
        view.table.setHorizontalHeaderItem(3,QTableWidgetItem('Existencias'))
        view.table.setHorizontalHeaderItem(4,QTableWidgetItem('Mínimo'))

        self.cur.execute(f"""SELECT PRODUCTOS.ID_PRODUCTO , PRODUCTOS.NOMBRE, PRODUCTOS.PRECIO, INVENTARIO.EXISTENCIAS , INVENTARIO.EXISTENCIAS_MIN
                         FROM PRODUCTOS INNER JOIN INVENTARIO ON 
                         PRODUCTOS.ID_PRODUCTO = INVENTARIO.ID_PRODUCTO WHERE ID_ALMACEN = {self.sede}""")

        productos = list(map(lambda reg: ProductoInventario(*reg),self.cur.fetchall()))
        view.table.setRowCount(len(productos))

        for i,producto in enumerate(productos):
            producto.desplegarFila(i,view.table)

    def seleccionarProveedor(self):
        self.dialog = QDialog()
        self.vistaSeleccionar = SeleccionarProveedor()
        self.vistaSeleccionar.setupUi(self.dialog,self)
        self.dialog.show()

    def consultarProveedores(self):
        self.cur.execute('SELECT * FROM PROVEEDORES')
        return list(map(lambda reg: Proveedor(*reg),self.cur.fetchall()))

    def generarOrdenDeCompra(self,proveedor):
        self.dialog = QDialog()
        self.ordenDeCompra = OrdenDeCompra()
        self.vistaOrdenDeCompra = OrdenCompra()
        self.vistaOrdenDeCompra.setupUi(self.dialog,self,proveedor)
        self.dialog.show()

    def confirmarCompra(self,proveedor):
        if(len(self.ordenDeCompra.productos)!=0):
            self.cur.execute(f"""INSERT INTO REGISTROS_COMPRA(PROVEEDOR, RESPONSABLE, FECHA) VALUES({proveedor.nit},{self.id}, datetime('now') )""")
            self.conexion.commit()

            self.cur.execute(f"""SELECT MAX(ID_OPERACION) FROM REGISTROS_COMPRA WHERE RESPONSABLE={self.id}""")
            idOperacion = self.cur.fetchall()[0][0]

            for producto in self.ordenDeCompra.productos:
                self.cur.execute(f"""INSERT INTO MOVIMIENTOS_INVENTARIO_COMPRA (ID_COMPRA, ID_PRODUCTO, CANTIDAD) VALUES({idOperacion},{producto.id},{producto.existencias})""")
                self.cur.execute(f"""UPDATE INVENTARIO
                                        SET EXISTENCIAS = EXISTENCIAS + {producto.existencias}
                                        WHERE ID_PRODUCTO = {producto.id} AND ID_ALMACEN={self.sede}""")

            
            self.conexion.commit()
            self.loadListaProductos(self.view)
            self.ordenDeCompra.productos = []


class UsuarioVendedor(Usuario):
    def __init__(self,usuario,nombre,cur,conexion):
        super().__init__(usuario,nombre,cur,conexion)
        self.factura = Factura()
        self.cur.execute(f'SELECT SEDE_TRABAJO FROM USUARIOS WHERE ID={self.id}')
        for reg in self.cur:
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

        self.cur.execute(f"""SELECT PRODUCTOS.ID_PRODUCTO , PRODUCTOS.NOMBRE, PRODUCTOS.PRECIO, INVENTARIO.EXISTENCIAS 
                         FROM PRODUCTOS INNER JOIN INVENTARIO ON 
                         PRODUCTOS.ID_PRODUCTO = INVENTARIO.ID_PRODUCTO WHERE ID_ALMACEN = {self.sede}""")

        self.productos = list(map(lambda reg: ProductoInventario(*reg),self.cur.fetchall()))
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
            self.cur.execute(f"""INSERT INTO REGISTROS_VENTA(RESPONSABLE, FECHA) VALUES({self.id}, datetime('now') )""")
            self.conexion.commit()

            self.cur.execute(f"""SELECT MAX(ID_OPERACION) FROM REGISTROS_VENTA WHERE RESPONSABLE={self.id}""")
            idOperacion = self.cur.fetchall()[0][0]

            for producto in self.factura.productos:
                print(f"""INSERT INTO MOVIMIENTOS_INVENTARIO_VENTA (ID_VENTA,ID_PRODUCTO,CANTIDAD) VALUES({idOperacion},{producto.id},{producto.existencias})""")
                self.cur.execute(f"""INSERT INTO MOVIMIENTOS_INVENTARIO_VENTA (ID_VENTA,ID_PRODUCTO,CANTIDAD) VALUES({idOperacion},{producto.id},{producto.existencias})""")
                self.cur.execute(f"""UPDATE INVENTARIO
                                        SET EXISTENCIAS = EXISTENCIAS - {producto.existencias}
                                        WHERE ID_PRODUCTO = {producto.id} AND ID_ALMACEN={self.sede}""")

            
            self.conexion.commit()
            self.loadListaProductos(self.view)
            self.factura.productos = []

def crearUsuario(ID,cursor,conexion):
    classes = [UsuarioVendedor,UsuarioAdministrativo,UsuarioSysAdmin]
    cursor.execute(f'SELECT NIVEL,NOMBRE FROM USUARIOS WHERE ID={ID}')
    nivel = 0
    nombre = ''
    for reg in cursor.fetchall():
        nivel = reg[0]
        nombre = reg[1]
    if(nombre!=''):
        return classes[nivel](ID,nombre,cursor,conexion)
