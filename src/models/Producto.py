from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QTableWidgetItem

class Producto:
    def __init__(self,_id,nombre,precio):
        self.id = _id
        self.nombre = nombre
        self.precio = precio

    def desplegarFila(self,i,table):
        column1 = QTableWidgetItem(str(self.id))
        column1.setTextAlignment(0x004)
        column3 = QTableWidgetItem(str(self.precio))
        column3.setTextAlignment(0x04)
        table.setItem(i,0,column1)
        table.setItem(i,1,QTableWidgetItem(self.nombre))
        table.setItem(i,2,column3)

class ProductoInventario(Producto):
    def __init__(self,_id,nombre,precio,existencias,existenciasMinimas=0):
        super().__init__(_id,nombre,precio)
        self.existencias = existencias
        self.existenciasMinimas = existenciasMinimas

    def desplegarFila(self,i,table):
        super().desplegarFila(i,table)
        column4 = QTableWidgetItem(str(self.existencias))
        column4.setTextAlignment(0x04)
        column5 = QTableWidgetItem(str(self.existenciasMinimas))
        column5.setTextAlignment(0x04)
        table.setItem(i,3,QTableWidgetItem(column4))
        table.setItem(i,4,QTableWidgetItem(column5))
        if(self.existencias<self.existenciasMinimas):
            for j in range(5):
               table.item(i,j).setBackground(QColor('#FF9999'))

    def desplegarFilaCompra(self,i,table):
        column1 = QTableWidgetItem(str(self.id))
        column1.setTextAlignment(0x004)
        column3 = QTableWidgetItem(str(self.existencias))
        column3.setTextAlignment(0x04)
        table.setItem(i,0,column1)
        table.setItem(i,1,QTableWidgetItem(self.nombre))
        table.setItem(i,2,column3)
