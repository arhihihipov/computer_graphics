from PyQt6.QtOpenGLWidgets import QOpenGLWidget
from OpenGL import GL as gl
from PyQt6 import QtCore
from geometry import median_dots, bisectors_intersection_dot, divide_cutoff


class glWidget(QOpenGLWidget):
    def __init__(self, main_window):
        super().__init__(parent=main_window.ui.centralwidget)
        # Ссылка на родительское окно
        self.mw = main_window
        # Массив точек, которые мы будем соединять
        self.points = []
        # Старые треугольники
        self.old_triangles = []
        # Новые треугольники
        self.new_triangles = []
        # начальный треугольник
        self.start = [[-1, 2 / 3 ** (1 / 2) - 1 + 0.5], [-1, -1 + 0.5], [1, -1 + 0.5]]

        main_window.ui.openGLWidget = self
        main_window.ui.openGLWidget.setGeometry(QtCore.QRect(10, 10, 600, 600))
        main_window.ui.openGLWidget.setObjectName("openGLWidget")

    # Настройка состояния. Вызывается один раз в самом начале
    def initializeGL(self):
        gl.glClearColor(0, 0, 0, 1)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

    def paintGL(self):
        self.points = []
        self.old_triangles = []
        self.new_triangles = []

        self.draw_fractal(self.start, self.mw.ui.horizontalSlider.value())

        gl.glLineWidth(1)
        # Рисование треугольников
        gl.glBegin(gl.GL_LINE_STRIP)
        gl.glColor3f(0.00, 0.5, 1)
        for triangle in self.old_triangles:
            for point in triangle:
                gl.glVertex2fv(point)
        for point in self.start:
            gl.glVertex2fv(point)
        gl.glEnd()

        gl.glLineWidth(3)
        # Рисование точек
        gl.glColor3f(1, 1, 1)
        gl.glBegin(gl.GL_LINE_STRIP)
        for point in self.points:
            gl.glVertex2fv(point)
        gl.glEnd()

    def count_triangles(self, dots):
        return [
            [divide_cutoff(dots[1], dots[2]), dots[1], dots[0]],
            [divide_cutoff(dots[1], dots[2]), median_dots([dots[0], dots[2]]), dots[0]],
            [divide_cutoff(dots[1], dots[2]), median_dots([dots[0], dots[2]]), dots[2]]
        ]

    def draw_fractal(self, dots, iterator):
        self.old_triangles.append(dots)
        for _ in range(iterator):
            for index,triangle in enumerate(self.old_triangles):
                res = self.count_triangles(triangle)
                if index % 2 != 0:
                    res.reverse()
                self.new_triangles += res
            self.old_triangles = self.new_triangles
            self.new_triangles = []
        for triangle in self.old_triangles:
            self.points.append(bisectors_intersection_dot(triangle))
