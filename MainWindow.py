import sys
from PyQt6.QtWidgets import  QMainWindow, QRubberBand
from glWidget import glWidget
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Создание виджета для отображения графики
        self.ui.openGLWidget = glWidget(self)

        #Обработка событий
        self.ui.pushButton.clicked.connect(self.quit)
        self.ui.horizontalSlider.valueChanged.connect(self.indicate)

        # Демонстрация окна
        self.show()

    def quit(self):
        sys.exit()

    def indicate(self):
        self.ui.openGLWidget.update()
