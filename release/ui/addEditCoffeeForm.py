# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(408, 300)
        self.nameEdit = QtWidgets.QLineEdit(parent=Form)
        self.nameEdit.setGeometry(QtCore.QRect(280, 20, 113, 21))
        self.nameEdit.setObjectName("nameEdit")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(10, 20, 131, 16))
        self.label.setObjectName("label")
        self.degreeEdit = QtWidgets.QLineEdit(parent=Form)
        self.degreeEdit.setGeometry(QtCore.QRect(280, 50, 113, 21))
        self.degreeEdit.setText("")
        self.degreeEdit.setObjectName("degreeEdit")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 131, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 131, 16))
        self.label_3.setObjectName("label_3")
        self.groundbeansEdit = QtWidgets.QLineEdit(parent=Form)
        self.groundbeansEdit.setGeometry(QtCore.QRect(280, 80, 113, 21))
        self.groundbeansEdit.setObjectName("groundbeansEdit")
        self.tasteEdit = QtWidgets.QLineEdit(parent=Form)
        self.tasteEdit.setGeometry(QtCore.QRect(280, 110, 113, 21))
        self.tasteEdit.setText("")
        self.tasteEdit.setObjectName("tasteEdit")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 131, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setGeometry(QtCore.QRect(10, 170, 131, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=Form)
        self.label_6.setGeometry(QtCore.QRect(10, 140, 131, 16))
        self.label_6.setObjectName("label_6")
        self.priceEdit = QtWidgets.QLineEdit(parent=Form)
        self.priceEdit.setGeometry(QtCore.QRect(280, 140, 113, 21))
        self.priceEdit.setObjectName("priceEdit")
        self.volumeEdit = QtWidgets.QLineEdit(parent=Form)
        self.volumeEdit.setGeometry(QtCore.QRect(280, 170, 113, 21))
        self.volumeEdit.setText("")
        self.volumeEdit.setObjectName("volumeEdit")
        self.sendButton = QtWidgets.QPushButton(parent=Form)
        self.sendButton.setGeometry(QtCore.QRect(280, 260, 113, 32))
        self.sendButton.setObjectName("sendButton")
        self.clearButton = QtWidgets.QPushButton(parent=Form)
        self.clearButton.setGeometry(QtCore.QRect(160, 260, 113, 32))
        self.clearButton.setObjectName("clearButton")
        self.resultLabel = QtWidgets.QLabel(parent=Form)
        self.resultLabel.setGeometry(QtCore.QRect(10, 200, 381, 41))
        self.resultLabel.setText("")
        self.resultLabel.setWordWrap(True)
        self.resultLabel.setObjectName("resultLabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Название сорта"))
        self.label_2.setText(_translate("Form", "Степень обжарки"))
        self.label_3.setText(_translate("Form", "Описание вкуса"))
        self.label_4.setText(_translate("Form", "Молотый/в зернах"))
        self.label_5.setText(_translate("Form", "Объем упаковки"))
        self.label_6.setText(_translate("Form", "Цена"))
        self.sendButton.setText(_translate("Form", "Отправить"))
        self.clearButton.setText(_translate("Form", "Очистить"))