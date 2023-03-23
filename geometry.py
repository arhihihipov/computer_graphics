import numpy as np
import math

# Поиск длины отрезка по его координатам
def find_len(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# Поиск середины отрезка cut
def median_dots(cut):
    return (cut[0][0] + cut[1][0]) / 2, (cut[0][1] + cut[1][1]) / 2

# Поиск точки пересечения биссектрис треугольника с заданными вершинами (центр вписанной окружности)
def bisectors_intersection_dot(triangle_dots):
    A = triangle_dots[0]
    B = triangle_dots[1]
    C = triangle_dots[2]
    O = [0,0]

    OA = np.array([A[0] - O[0], A[1] - O[1]])
    OB = np.array([B[0] - O[0], B[1] - O[1]])
    OC = np.array([C[0] - O[0], C[1] - O[1]])
    a = find_len(B, C)
    b = find_len(A, C)
    c = find_len(A, B)
    OI = (a * OA + b * OB + c * OC) / (a + b + c)
    return OI[0], OI[1]

# Найти точку, которая делит заданный отрезок в определённом соотношении
def divide_cutoff(A, B, ratio = 1/2):
    x = (A[0] + ratio * B[0]) / (1 + ratio)
    y = (A[1] + ratio * B[1]) / (1 + ratio)
    return x,y
