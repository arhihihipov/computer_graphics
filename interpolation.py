h00 = lambda t: 2 * t ** 3 - 3 * t ** 2 + 1
h10 = lambda t: t ** 3 - 2 * t ** 2 + t
h01 = lambda t: - 2 * t ** 3 + 3 * t ** 2
h11 = lambda t: t ** 3 - t ** 2


def kochanek_bartels_spline(points, t, b, c):
    new_points = []
    for i in range(1, len(points) - 2):
        x_i, p_i = points[i]
        p_i_prev = points[i-1][1]
        x_i1, p_i1 = points[i+1]
        p_i1_next = points[i + 2][1]

        # Считаем касательные
        d_i = (1-t)*(1+b)*(1+c)/2 * (p_i - p_i_prev) + (1-t)*(1-b)*(1-c)/2 * (p_i1 - p_i)
        d_i1 = (1-t)*(1+b)*(1-c)/2 * (p_i1 - p_i) + (1-t)*(1-b)*(1+c)/2 * (p_i1_next - p_i1)

        delta = (x_i1 - x_i)/20
        for i in range(21):
            current_point_x = x_i + i*delta
            t_p = (i*delta) / (x_i1 - x_i)
            #current_point_y = h00(t_p)*p_i + h10(t_p)*(x_i1 - x_i)*d_i + h01(t_p)*p_i1 + h11(t_p)*(x_i1 - x_i)*d_i1
            current_point_y = h00(t_p)*p_i + h10(t_p)*(x_i1 - x_i)*d_i/ abs(x_i - x_i1) + h01(t_p)*p_i1 + h11(t_p)*(x_i1 - x_i)*d_i1/ abs(x_i1 - x_i)
            new_points.append([current_point_x, current_point_y])

    return new_points

