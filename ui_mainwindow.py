# Form implementation generated from reading ui file 'ui_mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtOpenGLWidgets import QOpenGLWidget
from glWidget import glWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.openGLWidget = None
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(957, 671)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(840, 620, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Jura")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(650, 50, 281, 501))
        font = QtGui.QFont()
        font.setFamily("Jura")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.comboBox = QtWidgets.QComboBox(parent=self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(10, 30, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 110, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalSlider = QtWidgets.QSlider(parent=self.groupBox)
        self.horizontalSlider.setGeometry(QtCore.QRect(10, 200, 160, 22))
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(15)
        self.horizontalSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider_2 = QtWidgets.QSlider(parent=self.groupBox)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(10, 290, 160, 22))
        self.horizontalSlider_2.setMinimum(1)
        self.horizontalSlider_2.setMaximum(15)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider_3 = QtWidgets.QSlider(parent=self.groupBox)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(10, 370, 160, 22))
        self.horizontalSlider_3.setMinimum(1)
        self.horizontalSlider_3.setMaximum(20)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 170, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 260, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 340, 261, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "lab1_Arkhipov"))
        self.pushButton.setText(_translate("MainWindow", "Выход"))
        self.groupBox.setTitle(_translate("MainWindow", "Настройки"))
        self.comboBox.setItemText(0, _translate("MainWindow", "GL_POINT"))
        self.comboBox.setItemText(1, _translate("MainWindow", "GL_LINES"))
        self.comboBox.setItemText(2, _translate("MainWindow", "GL_LINE_STRIP"))
        self.comboBox.setItemText(3, _translate("MainWindow", "GL_LINE_LOOP"))
        self.comboBox.setItemText(4, _translate("MainWindow", "GL_TRIANGLES"))
        self.comboBox.setItemText(5, _translate("MainWindow", "GL_TRIANGLE_STRIP"))
        self.comboBox.setItemText(6, _translate("MainWindow", "GL_TRIANGLE_FAN"))
        self.comboBox.setItemText(7, _translate("MainWindow", "GL_QUADS"))
        self.comboBox.setItemText(8, _translate("MainWindow", "GL_QUAD_STRIP"))
        self.comboBox.setItemText(9, _translate("MainWindow", "GL_POLYGON"))
        self.pushButton_2.setText(_translate("MainWindow", "Изобразить"))
        self.label_2.setText(_translate("MainWindow", "Выберите размер точки"))
        self.label_3.setText(_translate("MainWindow", "Выберите толщину линии"))
        self.label_4.setText(_translate("MainWindow", "Выберите количество объектов"))