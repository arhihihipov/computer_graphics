# Form implementation generated from reading ui file 'ui_mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self):
        self.openGLWidget = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(975, 679)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(870, 640, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Jura")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(750, 360, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Jura")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(670, 70, 241, 80))
        font = QtGui.QFont()
        font.setFamily("Jura")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.tSlider = QtWidgets.QSlider(parent=self.groupBox)
        self.tSlider.setGeometry(QtCore.QRect(20, 40, 211, 22))
        self.tSlider.setMinimum(-100)
        self.tSlider.setMaximum(100)
        self.tSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.tSlider.setInvertedAppearance(False)
        self.tSlider.setInvertedControls(False)
        self.tSlider.setTickPosition(QtWidgets.QSlider.TickPosition.NoTicks)
        self.tSlider.setObjectName("tSlider")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(670, 250, 241, 80))
        font = QtGui.QFont()
        font.setFamily("Jura")
        font.setPointSize(12)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.cSlider = QtWidgets.QSlider(parent=self.groupBox_3)
        self.cSlider.setGeometry(QtCore.QRect(20, 40, 211, 22))
        self.cSlider.setMinimum(-100)
        self.cSlider.setMaximum(100)
        self.cSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.cSlider.setInvertedAppearance(False)
        self.cSlider.setInvertedControls(False)
        self.cSlider.setTickPosition(QtWidgets.QSlider.TickPosition.NoTicks)
        self.cSlider.setObjectName("cSlider")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(670, 160, 241, 80))
        font = QtGui.QFont()
        font.setFamily("Jura")
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.bSlider = QtWidgets.QSlider(parent=self.groupBox_2)
        self.bSlider.setGeometry(QtCore.QRect(20, 40, 211, 22))
        self.bSlider.setMinimum(-100)
        self.bSlider.setMaximum(100)
        self.bSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.bSlider.setInvertedAppearance(False)
        self.bSlider.setInvertedControls(False)
        self.bSlider.setTickPosition(QtWidgets.QSlider.TickPosition.NoTicks)
        self.bSlider.setObjectName("bSlider")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Arkhipov_0303_lab4"))
        self.pushButton.setText(_translate("MainWindow", "Выход"))
        self.pushButton_2.setText(_translate("MainWindow", "Сброс"))
        self.groupBox.setTitle(_translate("MainWindow", "Натяжение t"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Непрерывность c"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Смещение b"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
