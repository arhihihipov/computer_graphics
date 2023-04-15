import sys
from PyQt6.QtWidgets import  QMainWindow
from glWidget import glWidget
from ui_mainwindow import Ui_MainWindow

from OpenGL import GL as gl
from time import sleep


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Создание виджета для отображения графики
        self.ui.openGLWidget = glWidget(self)

        # Подписка элементов интерфейса на события
        self.ui.pushButton.clicked.connect(self.leave)


        self.ui.openGLWidget.update()



        # Демонстрация окна
        self.show()


    def leave(self):
        print('You entered "Quit" button')
        sys.exit()




