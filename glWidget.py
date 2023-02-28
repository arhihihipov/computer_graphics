from PyQt6.QtOpenGLWidgets import QOpenGLWidget
from OpenGL import GL as gl
from PyQt6 import QtCore
from random import uniform

class glWidget(QOpenGLWidget):
    def __init__(self, main_window):
        super().__init__(parent=main_window.ui.centralwidget)
        # Примитив, который будет нарисован
        self.primitive = None
        # Минимальное количество точек, которое может быть в примитиве
        self.minPoints = None
        # Флаг, содержащий информацию о том, нужно ли вычислять точки заново
        self.makeNewPoints = False
        # Ссылка на родительское окно
        self.mw = main_window

        main_window.ui.openGLWidget = self
        main_window.ui.openGLWidget.setGeometry(QtCore.QRect(20, 50, 600, 600))
        main_window.ui.openGLWidget.setObjectName("openGLWidget")

    # Настройка состояния. Вызывается один раз в самом начале
    def initializeGL(self):
        gl.glClearColor(0, 0, 0, 1)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

    def paintGL(self):
        if self.primitive != None:
            # Генерация новых точек, если это необходимо
            if self.makeNewPoints:
                objectsCounter = self.mw.ui.horizontalSlider_3.value()
                self.points = [[uniform(-0.99,0.99), uniform(-0.99, 0.99)] for _ in range(objectsCounter * self.minPoints)]

                # Обрезание массива точек
                if self.primitive in [gl.GL_LINE_STRIP, gl.GL_LINE_LOOP]:
                    self.points = self.points[:objectsCounter + 1]
                elif self.primitive in [gl.GL_TRIANGLE_STRIP, gl.GL_TRIANGLE_FAN]:
                    self.points = self.points[:objectsCounter + 2]
                elif self.primitive in [gl.GL_QUAD_STRIP]:
                    self.points = self.points[: 2 * (objectsCounter + 1)]

                # Генерация цветов точек
                self.colors = [[uniform(0, 1) for i in range(3)] for _ in range(len(self.points))]

            # Установка размера точки
            gl.glPointSize(self.mw.ui.horizontalSlider.value())
            # Установка толщины линии
            gl.glLineWidth(self.mw.ui.horizontalSlider_2.value())

            # Рисование
            gl.glBegin(self.primitive)
            for index, point in enumerate(self.points):
                if index % self.minPoints == 0:
                    gl.glColor3fv(self.colors[index])
                gl.glVertex2fv(point)
            gl.glEnd()

