from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QByteArray
from PyQt5.QtGui import QPixmap
from PIL import Image

class Ui_Image(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(621, 454)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 2, 631, 451))
        self.label.setText("")
        self.label.setObjectName("label")
        # self.pushButton = QtWidgets.QPushButton(Dialog)
        # self.pushButton.setGeometry(QtCore.QRect(250, 400, 111, 31))
        # self.pushButton.setObjectName("pushButton")

        pixmap = QPixmap(Dialog.image)
        self.label.setPixmap(pixmap.scaled(611, 431))

        # image = QtGui.QImage(bytes(Dialog.image), 611, 431, QtGui.QImage.Format_Indexed8)
        # pixmap = QPixmap(image)
        # self.label.setPixmap(pixmap)#.scaled(611, 431))


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        # self.pushButton.setText(_translate("Dialog", "NEXT"))
        # self.pushButton.clicked.connect()
