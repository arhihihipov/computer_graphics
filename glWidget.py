from PyQt6.QtOpenGLWidgets import QOpenGLWidget
from OpenGL import GL as gl
from OpenGL.GL.shaders import compileShader, compileProgram
from PyQt6 import QtCore

# Функция для чтения содержимого файла
def read_file(file_name, descriptor='r'):
    file = open(file_name, descriptor)
    content = file.read()
    return content

class glWidget(QOpenGLWidget):
    def __init__(self, main_window):
        super().__init__(parent=main_window.ui.centralwidget)
        # Ссылка на родительское окно
        self.mw = main_window

        self.vertex = [[-1, -1],[1, -1],[0, 1]]

        self.demo = 2

        if self.demo == 1:
            self.colors = [[1, 0, 0],[0, 1, 0],[0, 0, 1]]
        elif self.demo == 2:
            self.colors = [[x / 255 for x in [176, 201, 230]], [x / 255 for x in [250, 128, 114]],
                           [x / 255 for x in [245, 255, 250]]]
        elif self.demo == 3:
            self.colors = [[x / 255 for x in [187, 38, 73]], [x / 255 for x in [128, 0, 0]],
                           [x / 255 for x in [220, 20, 60]]]
        else:
            self.colors = [[1, 0, 0], [1, 0, 0], [0, 0, 0]]

        main_window.ui.openGLWidget = self
        main_window.ui.openGLWidget.setGeometry(QtCore.QRect(10, 10, 600, 600))
        main_window.ui.openGLWidget.setObjectName("openGLWidget")


    # Настройка состояния. Вызывается один раз в самом начале
    def initializeGL(self):
        gl.glClearColor(1, 1, 1, 1)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

        self.shader = compileProgram(compileShader(read_file('fragment_shader.frag'), gl.GL_FRAGMENT_SHADER))

        vertex_a = gl.glGetUniformLocation(self.shader, 'A')
        vertex_b = gl.glGetUniformLocation(self.shader, 'B')
        vertex_c = gl.glGetUniformLocation(self.shader, 'C')

        vertex_a_color = gl.glGetUniformLocation(self.shader, 'A_color')
        vertex_b_color = gl.glGetUniformLocation(self.shader, 'B_color')
        vertex_c_color = gl.glGetUniformLocation(self.shader, 'C_color')




        gl.glUseProgram(self.shader)


        gl.glUniform2f(vertex_a, *self.vertex[0])
        gl.glUniform2f(vertex_b, *self.vertex[1])
        gl.glUniform2f(vertex_c, *self.vertex[2])
        gl.glUniform3f(vertex_a_color, *self.colors[0])
        gl.glUniform3f(vertex_b_color, *self.colors[1])
        gl.glUniform3f(vertex_c_color, *self.colors[2])


    def paintGL(self):
        gl.glPointSize(5)
        gl.glBegin(gl.GL_TRIANGLES)
        for i in range(3):
            gl.glColor3fv(self.colors[i])
            gl.glVertex2fv(self.vertex[i])
        gl.glEnd()
