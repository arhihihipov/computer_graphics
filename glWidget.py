from PyQt6.QtOpenGLWidgets import QOpenGLWidget
from OpenGL import GL as gl
from PyQt6 import QtCore
from random import uniform
import math
from PyQt6.QtWidgets import QRubberBand
from PyQt6.QtCore import QSize, QRect


class glWidget(QOpenGLWidget):
    def __init__(self, main_window):
        super().__init__(parent=main_window.ui.centralwidget)
        # Примитив, который будет нарисован
        self.primitive = None
        # Флаг, содержащий информацию о том, нужно ли вычислять точки заново
        self.makeNewPoints = False
        # Ссылка на родительское окно
        self.mw = main_window
        # Параметры для ножниц
        self.scissors = [0, 0, 0, 0]
        # Флаг для ножниц
        self.scissors_test = False
        # Область выбора
        self.rubberBand = None

        main_window.ui.openGLWidget = self
        main_window.ui.openGLWidget.setGeometry(QtCore.QRect(20, 50, 600, 600))
        main_window.ui.openGLWidget.setObjectName("openGLWidget")

    # Настройка состояния. Вызывается один раз в самом начале
    def initializeGL(self):
        gl.glClearColor(0, 0, 0, 1)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

    def paintGL(self):
        if self.primitive != None:
            # Тест отсечения
            if self.scissors_test and self.scissors[2:4] != [0, 0]:
                gl.glEnable(gl.GL_SCISSOR_TEST)
                gl.glScissor(int(self.scissors[0] * 750 / 600), int(self.scissors[1] * 750 / 600),
                             int(self.scissors[2] * 750 / 600), int(self.scissors[3] * 750 / 600))
            else:
                gl.glDisable(gl.GL_SCISSOR_TEST)
                # gl.glScissor(0, 0, 750, 750)

            # Тест прозрачности
            if self.mw.ui.checkBox_2.isChecked():
                gl.glEnable(gl.GL_ALPHA_TEST)
                gl.glAlphaFunc(self.mw.transparency[self.mw.ui.comboBox_2.currentIndex()],
                               self.mw.ui.horizontalSlider_3.value() / 100)
            else:
                gl.glDisable(gl.GL_ALPHA_TEST)

            # Тест смешение цветов
            if self.mw.ui.checkBox_3.isChecked():
                gl.glEnable(gl.GL_BLEND)
                gl.glBlendFunc(self.mw.sfactor[self.mw.ui.comboBox_4.currentIndex()],
                               self.mw.dfactor[self.mw.ui.comboBox_3.currentIndex()])
            else:
                gl.glDisable(gl.GL_BLEND)

            self.draw_primitive()

            # От диагонали к диагонали
            # if self.scissors_test:
            #     self.scissors_test = False
            #     gl.glDisable(gl.GL_SCISSOR_TEST)

    # Функция для рисования примитивов
    def draw_primitive(self):
        if self.primitive != "CIRCLES":
            if self.makeNewPoints:
                # Генерация новых точек, если это необходимо
                self.points = [[uniform(-0.99, 0.99), uniform(-0.99, 0.99)] for _ in range(12)]
                # Генерация цветов точек
                self.colors = [[uniform(0, 1) for i in range(4)] for _ in range(len(self.points))]

            # Установка размера точки
            gl.glPointSize(5)
            # Установка толщины линии
            gl.glLineWidth(5)

            # Рисование
            gl.glBegin(self.primitive)
            for index, point in enumerate(self.points):
                gl.glColor4fv(self.colors[index])
                gl.glVertex2fv(point)
            gl.glEnd()

        elif self.primitive == "CIRCLES":
            self.draw_circles()

        self.makeNewPoints = False

    def draw_circles(self):
        for color, pos_x_y in zip([[1, 0, 0, 0.6], [0, 1, 0, 0.9], [0, 0, 1, 0.7]],
                                  [[-0.3, -0.3], [0.3, -0.3], [0, 0.3]]):
            steps = 200
            radius = 0.6
            a = math.pi * 2 / steps

            gl.glBegin(gl.GL_TRIANGLE_FAN)
            gl.glColor4fv(color)
            gl.glVertex2fv(pos_x_y)
            for i in range(steps + 1):
                x = pos_x_y[0] + math.sin(a * i) * radius
                y = pos_x_y[1] + math.cos(a * i) * radius
                gl.glVertex2f(x, y)
            gl.glEnd()

    # Окно с выбором для обрезания
    def mousePressEvent(self, event):
        if self.mw.ui.checkBox.isChecked():
            self.origin = event.pos()

            self.scissors[0] = self.origin.x()
            self.scissors[1] = self.origin.y()

            if not self.rubberBand:
                self.rubberBand = QRubberBand(QRubberBand.Shape.Rectangle, self)
            self.rubberBand.setGeometry(QRect(self.origin, QSize()))
            self.rubberBand.show()

    def mouseMoveEvent(self, event):
        if self.mw.ui.checkBox.isChecked():
            self.rubberBand.setGeometry(QRect(self.origin, event.pos()).normalized())

    def mouseReleaseEvent(self, event):
        if self.mw.ui.checkBox.isChecked():
            if event.pos().x() < 0:
                width = abs(self.scissors[0])
            elif event.pos().x() > 600:
                width = abs(600 - self.scissors[0])
            else:
                width = abs(self.scissors[0] - event.pos().x())

            if event.pos().y() < 0:
                height = abs(self.scissors[1])
            elif event.pos().y() > 600:
                height = abs(600 - self.scissors[1])
            else:
                height = abs(event.pos().y() - self.scissors[1])

            self.scissors[0] = min(self.scissors[0], event.pos().x())
            self.scissors[1] = 600 - max(self.scissors[1], event.pos().y())
            self.scissors[2] = width
            self.scissors[3] = height

            self.rubberBand.hide()
            if height * width != 0:
                self.scissors_test = True
                self.update()