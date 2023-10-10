#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main(void) {
    double temp_c, temp_f;
    system("clear");
    printf("Enter the value of temperature in °C\n");
    scanf("%lf",&temp_c);
    temp_f = (temp_c * 9) / 5;
    temp_f = temp_f + 32;
    printf("The temperature is %lf°F\n", temp_f);
    getchar();
    return 0;
}