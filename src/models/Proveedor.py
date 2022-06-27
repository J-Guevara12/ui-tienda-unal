from PyQt5.QtWidgets import QTableWidgetItem

class Proveedor:
    def __init__(self,nit,empresa,contacto,email,telefono):
        self.nit = nit
        self.empresa = empresa
        self.contacto = contacto
        self.email = email
        self.telefono = telefono

    def desplegarFila(self,i,table):
        table.setItem(i,0,QTableWidgetItem(str(self.nit)))
        table.setItem(i,1,QTableWidgetItem(str(self.empresa)))
        table.setItem(i,2,QTableWidgetItem(str(self.contacto)))
        table.setItem(i,3,QTableWidgetItem(str(self.email)))
        table.setItem(i,4,QTableWidgetItem(str(self.telefono)))
