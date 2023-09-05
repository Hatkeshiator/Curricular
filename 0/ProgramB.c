#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main(void) {
    double a, b;
    system("clear");
    printf("Please enter two numbers:\n");
    scanf("%lf%lf", &a, &b);
    printf("The result of the following operations on these numbers is:\nAddition: %lf\nSubtraction: %lf\nDivision: %lf (Reciprocal: %lf)\nMultiplication: %lf\n", a + b, a - b, a / b, b / a, a * b);
    getchar();
    return 0;
}