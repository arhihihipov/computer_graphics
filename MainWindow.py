import sys
from PyQt6.QtWidgets import  QMainWindow
from glWidget import glWidget
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Создание виджета для отображения графики
        self.ui.openGLWidget = glWidget(self)

        # Подписка элементов интерфейса на события
        self.ui.pushButton.clicked.connect(self.leave)
        self.ui.tSlider.valueChanged.connect(self.param_changed)
        self.ui.bSlider.valueChanged.connect(self.param_changed)
        self.ui.cSlider.valueChanged.connect(self.param_changed)
        self.ui.pushButton_2.clicked.connect(self.restart)

        # Демонстрация окна
        self.show()


    def leave(self):
        print('Выполнен выход из приложения')
        sys.exit()

    def param_changed(self):
        self.ui.openGLWidget.update()

    def restart(self):
        print('Выполним сброс точек')
        self.ui.openGLWidget.points = []
        self.ui.tSlider.setValue(0)
        self.ui.cSlider.setValue(0)
        self.ui.bSlider.setValue(0)
        self.ui.openGLWidget.update()
