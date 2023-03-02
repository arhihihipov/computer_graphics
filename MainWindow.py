import sys
from PyQt6.QtWidgets import  QMainWindow, QRubberBand
from glWidget import glWidget
from ui_mainwindow import Ui_MainWindow
from OpenGL import GL as gl
from PyQt6.QtCore import QSize, QRect, Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Создание виджета для отображения графики
        self.ui.openGLWidget = glWidget(self)

        # Создание списка примитивов и минимального числа точек, необходимого для их построения
        self.primitives = [
            gl.GL_POINTS,
            gl.GL_LINES,
            gl.GL_LINE_STRIP,
            gl.GL_LINE_LOOP,
            gl.GL_TRIANGLES,
            gl.GL_TRIANGLE_STRIP,
            gl.GL_TRIANGLE_FAN,
            gl.GL_QUADS,
            gl.GL_QUAD_STRIP,
            gl.GL_POLYGON,
            "CIRCLES"
        ]

        # Создание списка для теста прозрачности
        self.transparency = [
            gl.GL_NEVER,
            gl.GL_LESS,
            gl.GL_EQUAL,
            gl.GL_LEQUAL,
            gl.GL_GREATER,
            gl.GL_NOTEQUAL,
            gl.GL_GEQUAL,
            gl.GL_ALWAYS
        ]

        # Создание списка для sfactor
        self.sfactor = [
            gl.GL_ZERO,
            gl.GL_ONE,
            gl.GL_DST_COLOR,
            gl.GL_ONE_MINUS_DST_COLOR,
            gl.GL_SRC_ALPHA,
            gl.GL_ONE_MINUS_SRC_ALPHA,
            gl.GL_DST_ALPHA,
            gl.GL_ONE_MINUS_DST_ALPHA,
            gl.GL_SRC_ALPHA_SATURATE
        ]

        # Создание списка для dfactor
        self.dfactor = [
            gl.GL_ZERO,
            gl.GL_ONE,
            gl.GL_SRC_COLOR,
            gl.GL_ONE_MINUS_SRC_COLOR,
            gl.GL_SRC_ALPHA,
            gl.GL_ONE_MINUS_SRC_ALPHA,
            gl.GL_DST_ALPHA,
            gl.GL_ONE_MINUS_DST_ALPHA
        ]


        #Обработка событий
        self.ui.pushButton.clicked.connect(self.quit)
        self.ui.comboBox.activated.connect(self.draw_primitive)

        # Тест отсечения
        self.ui.checkBox.stateChanged.connect(self.cutting)

        # Тест прозрачности
        self.ui.checkBox_2.stateChanged.connect(self.transparent)
        self.ui.comboBox_2.activated.connect(self.transparent)
        self.ui.horizontalSlider_3.valueChanged.connect(self.transparent)

        # Смешение цветов
        self.ui.checkBox_3.stateChanged.connect(self.blender)
        self.ui.comboBox_3.activated.connect(self.blender)
        self.ui.comboBox_4.activated.connect(self.blender)


        # Демонстрация окна
        self.show()

    # Выход из приложения
    def quit(self):
        sys.exit()

    # Рисование примитивов
    def draw_primitive(self, index):
        self.ui.openGLWidget.primitive = self.primitives[index]
        self.ui.openGLWidget.makeNewPoints = True
        self.ui.openGLWidget.scissors_test = False
        self.ui.openGLWidget.scissors = [0,0,0,0]

        # Сохранение обрезания
        # if self.ui.checkBox.isChecked():
        #     self.ui.openGLWidget.scissors_test = True

        self.ui.openGLWidget.update()

    # Тест отсечения
    def cutting(self, value):
        if value == 2:
            self.ui.openGLWidget.scissors_test = True
        else:
            self.ui.openGLWidget.scissors_test = False
            self.ui.openGLWidget.scissors = [0,0,0,0]
        self.ui.openGLWidget.makeNewPoints = False
        self.ui.openGLWidget.update()

    # Тест прозрачности
    def transparent(self):
        self.ui.openGLWidget.update()

    # Тест смешения цветов
    def blender(self):
        self.ui.openGLWidget.update()


