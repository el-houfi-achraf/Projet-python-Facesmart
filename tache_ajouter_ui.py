# Form implementation generated from reading ui file 'c:\Users\Hp\Desktop\projet-pfa-2\tache_ajouter.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(832, 520)
        Dialog.setStyleSheet("background-color:#CDBEFF;")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(260, 30, 391, 461))
        self.label_2.setStyleSheet("border: 2px solid rgba(0, 0, 0, 255);\n"
"border-radius: 30px;\n"
"background-color:#332562;\n"
"\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(parent=Dialog)
        self.label_7.setGeometry(QtCore.QRect(430, 40, 121, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(-1)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:70px;\n"
"")
        self.label_7.setObjectName("label_7")
        self.pushButton_3 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 170, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:20px;\n"
"border:none;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(260, 280, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:20px;\n"
"border:none;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(290, 220, 321, 31))
        self.lineEdit_3.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:20px;\n"
"border:none;\n"
"border-bottom: 2px solid #FFFFFF;")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.comboBox = QtWidgets.QComboBox(parent=Dialog)
        self.comboBox.setGeometry(QtCore.QRect(290, 330, 331, 31))
        self.comboBox.setStyleSheet("background-color:#332562;\n"
"color:#FFFFFF;\n"
"font-size:20px;\n"
"border:none;\n"
"border-bottom: 2px solid #FFFFFF;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(380, 410, 141, 41))
        self.pushButton.setStyleSheet("\n"
"font-size:20px;\n"
"border:none;\n"
"border: 2px solid #FFFFFF;\n"
"border-radius: 10px;")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_7.setText(_translate("Dialog", ""))
        self.pushButton_3.setText(_translate("Dialog", "Nom Tache :"))
        self.pushButton_4.setText(_translate("Dialog", "Statue :"))
        self.comboBox.setItemText(0, _translate("Dialog", "en cours"))
        self.comboBox.setItemText(1, _translate("Dialog", "terminée"))
        self.comboBox.setItemText(2, _translate("Dialog", "à faire"))
        self.comboBox.setItemText(3, _translate("Dialog", "suspendue"))
        self.pushButton.setText(_translate("Dialog", "Ajouter"))
