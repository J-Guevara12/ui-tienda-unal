# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editarProducto.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 500)
        self.IDLabel = QtWidgets.QLabel(Dialog)
        self.IDLabel.setGeometry(QtCore.QRect(290, 130, 231, 24))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.IDLabel.setFont(font)
        self.IDLabel.setText("")
        self.IDLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.IDLabel.setObjectName("IDLabel")
        self.inputNombre = QtWidgets.QLineEdit(Dialog)
        self.inputNombre.setGeometry(QtCore.QRect(350, 200, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.inputNombre.setFont(font)
        self.inputNombre.setObjectName("inputNombre")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(210, 280, 91, 24))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(210, 210, 111, 22))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.inputPrecio = QtWidgets.QLineEdit(Dialog)
        self.inputPrecio.setGeometry(QtCore.QRect(350, 270, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.inputPrecio.setFont(font)
        self.inputPrecio.setObjectName("inputPrecio")
        self.confirmar = QtWidgets.QPushButton(Dialog)
        self.confirmar.setGeometry(QtCore.QRect(660, 450, 120, 35))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(230, 255, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 255, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 255, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.confirmar.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.confirmar.setFont(font)
        self.confirmar.setObjectName("confirmar")
        self.cancelar = QtWidgets.QPushButton(Dialog)
        self.cancelar.setGeometry(QtCore.QRect(510, 450, 120, 35))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 203, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(147, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 203, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(147, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 203, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.cancelar.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.cancelar.setFont(font)
        self.cancelar.setObjectName("cancelar")
        self.inventario = QtWidgets.QPushButton(Dialog)
        self.inventario.setGeometry(QtCore.QRect(20, 430, 161, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(231, 255, 253))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 49, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 255, 253))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 49, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 255, 253))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.inventario.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.inventario.setFont(font)
        self.inventario.setAutoFillBackground(False)
        self.inventario.setObjectName("inventario")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Precio"))
        self.label_2.setText(_translate("Dialog", "Nombre"))
        self.confirmar.setText(_translate("Dialog", "OK"))
        self.cancelar.setText(_translate("Dialog", "Cancelar"))
        self.inventario.setText(_translate("Dialog", "Editar existencias"))