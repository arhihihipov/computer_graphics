from PyQt6.QtOpenGLWidgets import QOpenGLWidget
from OpenGL import GL as gl
from PyQt6 import QtCore
from interpolation import kochanek_bartels_spline

class glWidget(QOpenGLWidget):
    def __init__(self, main_window):
        super().__init__(parent=main_window.ui.centralwidget)
        # Список, отмеченных пользователем точек
        self.points = []

        main_window.ui.openGLWidget = self
        main_window.ui.openGLWidget.setGeometry(QtCore.QRect(10, 10, 640, 640))
        main_window.ui.openGLWidget.setObjectName("openGLWidget")
        # Ссылка на родительское окно
        self.mw = main_window

    # Настройка состояния. Вызывается перед каждым обновлением кадра
    def initializeGL(self):
        gl.glClearColor(1,1,1,1)
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

    def paintGL(self):
        gl.glColor3f(1, 0, 0)
        gl.glPointSize(4)
        gl.glBegin(gl.GL_POINTS)
        if not self.points:
            gl.glColor3f(1,1,1)
            gl.glVertex2f(0,0)
        gl.glColor3f(0,0,0)
        for point in self.points:
            gl.glVertex2fv(point)
        gl.glEnd()

        if len(self.points) >=  4:
            gl.glColor3f(1.00,0.41,0.71)
            gl.glPointSize(2)
            gl.glLineWidth(2)
            gl.glBegin(gl.GL_LINE_STRIP)

            for point in kochanek_bartels_spline(self.points, self.mw.ui.tSlider.value()/100,
                                                 self.mw.ui.bSlider.value()/100, self.mw.ui.cSlider.value()/100):
                gl.glVertex2fv(point)
            gl.glEnd()

    # Клик мышки создаёт в этом месте точку
    def mousePressEvent(self, event):
        origin = event.pos()
        x = origin.x()
        y = origin.y()

        if x < 320:
            x = -(320 - x)/320
        else:
            x = (x - 320)/320

        if y < 320:
            y = (320 - y)/320
        else:
            y = -(y - 320) / 320

        point = [x, y]
        self.points.append(point)
        self.update()