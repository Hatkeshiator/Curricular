#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main(void) {
    double x, y, r, c, a;
    double P = 3.141592653;
    system("clear");
    printf("There exists a point on the catesian plane 4 units along the X axis and 5 units along the Y axis\nThis point will be the center of a circle. Give the coordinates x and y of a point on the circle's circumference and you will be told its radius, circumference, and area.\n");
    scanf("%lf%lf",&x,&y);
    x = abs(x - 4);
    y = abs(y - 5);
    r = sqrt((x * x) + (y * y));
    c = P * r * 2;
    a = P * r * r;
    printf("The radius of the circle is %lf\nIts circumference is %lf\nAnd its area is %lf\n", r, c, a);
    getchar();
    return 0;
}