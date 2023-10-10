#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main(void) {
    double x, y, r, c, a;
    double P = 3.141592653;
    x = 4.0;
    y = 5.0;
    r = x*x + y*y;
    r = sqrt(r);
    c = 2 * P * r;
    a = P * r * r;
    system("clear");
    printf("The radius of the circle = %lf\n", r);
    printf("Its circumference = %lf\n", c);
    printf("Its area = %lf\n", a);
    getchar();
    return 0;
}