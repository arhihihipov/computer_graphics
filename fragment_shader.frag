#version 430

out vec4 color;

uniform vec2 A;
uniform vec2 B;
uniform vec2 C;

uniform vec3 A_color;
uniform vec3 B_color;
uniform vec3 C_color;

struct line{
    vec2 p1;
    vec2 p2;
};

// Трансформация координат
vec2 transform_coords(vec4 point){
    float x = point.x;
    if (x < 375) {
        x = -((375 - x) / 375);
    } else {
        x = (x-375)/375;
    }

    float y = point.y;
    if (y<375){
        y = -(375-y)/375;
    } else {
        y = (y-375)/375;
    }

    return vec2(x, y);
}

// Расстояние между двумя точками
float get_distance(vec2 p1, vec2 p2){
    return sqrt(pow((p1.x - p2.x), 2.0) + pow((p1.y - p2.y), 2.0));
}

// Пересечение прямых l1 и l2
vec2 intersection(line l1, line l2){
    float d = (l2.p2.y - l2.p1.y) * (l1.p2.x - l1.p1.x) - (l2.p2.x - l2.p1.x) * (l1.p2.y - l1.p1.y);
    float a = (l2.p2.x - l2.p1.x) * (l1.p1.y - l2.p1.y) - (l2.p2.y - l2.p1.y) * (l1.p1.x - l2.p1.x);

    float x0 = l1.p1.x + a * (l1.p2.x-l1.p1.x)/d;
    float y0 = l1.p1.y + a * (l1.p2.y-l1.p1.y)/d;

    return vec2(x0,y0);
}

// Высота из точки point на прямую ln
line height(vec2 point, line ln){
    vec2 dir = vec2(0,0);
    dir.x = ln.p2.x - ln.p1.x;
    dir.y = ln.p2.y - ln.p1.y;

    vec2 point2 = vec2(0,0);
    if(dir.y != 0){
        float temp = dir.x*point.x + dir.y * point.y;
        point2.x = point.x != 1 ? 1 : 2;
        point2.y = (-dir.x * point2.x + temp) / dir.y;
    } else {
        point2.x = point.x;
        point2.y = ln.p1.y;
    }

    return line(point, intersection(ln, line(point, point2)));
}


void main()
{
    line AC = line(A, C);
    line AB = line(A, B);
    line CB = line(C, B);
    vec2 O = transform_coords(gl_FragCoord);

    // Высота из точки A на сторону BC
    line AH = height(A, CB);
    line O_AH = height(O, AH);
    float pA = 1 - get_distance(A, O_AH.p2)/ get_distance(A, AH.p2);

    // Высота из точки C на сторону AB
    line CH = height(C, AB);
    line O_CH = height(O, CH);
    float pC = 1- get_distance(C, O_CH.p2)/ get_distance(C, CH.p2);

    // Высота из точки B на сторону AC
    line BH = height(B,AC);
    line O_BH = height(O, BH);
    float pB = 1 - get_distance(B, O_BH.p2)/ get_distance(B, BH.p2);

    float red = (A_color.r * pA + B_color.r * pB + C_color.r * pC);
    float green = (A_color.g * pA + B_color.g * pB + C_color.g * pC);
    float blue = (A_color.b * pA + B_color.b * pB + C_color.b * pC);

    color = vec4(red, green, blue, 1);
}


