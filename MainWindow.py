import sys
from PyQt6.QtWidgets import  QMainWindow
from glWidget import glWidget
from ui_mainwindow import Ui_MainWindow
from OpenGL import GL as gl


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Создание виджета для отображения графики
        self.ui.openGLWidget = glWidget(self)

        # Подписка элементов интерфейса на события
        self.ui.pushButton.clicked.connect(self.leave)
        self.ui.pushButton_2.clicked.connect(self.draw)
        self.ui.horizontalSlider.valueChanged.connect(self.pointSizeChanged)
        self.ui.horizontalSlider_2.valueChanged.connect(self.lineWidthChanged)
        self.ui.horizontalSlider_3.valueChanged.connect(self.objectCounterChanged)

        # Создание словаря примитивов и минимального числа точек, необходимого для их построения
        self.functions = {
            "GL_POINT": [gl.GL_POINTS, 1],
            "GL_LINES": [gl.GL_LINES, 2],
            "GL_LINE_STRIP": [gl.GL_LINE_STRIP, 2],
            "GL_LINE_LOOP": [gl.GL_LINE_LOOP, 2],
            "GL_TRIANGLES": [gl.GL_TRIANGLES, 3],
            "GL_TRIANGLE_STRIP": [gl.GL_TRIANGLE_STRIP, 3],
            "GL_TRIANGLE_FAN": [gl.GL_TRIANGLE_FAN, 3],
            "GL_QUADS": [gl.GL_QUADS, 4],
            "GL_QUAD_STRIP": [gl.GL_QUAD_STRIP, 4],
            "GL_POLYGON": [gl.GL_POLYGON, 1]
        }
        self.dictionary = {count: elem for count, elem in enumerate(self.functions.keys())}

        # Демонстрация окна
        self.show()


    def leave(self):
        print('You entered "Quit" button')
        sys.exit()

    def draw(self):
        option = self.dictionary[self.ui.comboBox.currentIndex()]
        self.ui.openGLWidget.primitive, self.ui.openGLWidget.minPoints = self.functions[option]
        self.ui.openGLWidget.makeNewPoints = True
        self.ui.openGLWidget.update()

    def pointSizeChanged(self):
        self.ui.openGLWidget.makeNewPoints = False
        self.ui.openGLWidget.update()


    def lineWidthChanged(self):
        self.ui.openGLWidget.makeNewPoints = False
        self.ui.openGLWidget.update()

    def objectCounterChanged(self):
        self.ui.openGLWidget.makeNewPoints = True
        self.ui.openGLWidget.update()