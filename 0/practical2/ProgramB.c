/*
    Given $s = ut + frac{1}{2} \cdot a \cdot t^{2}$ \\
    take as input the time interval of user's selection \\
    and output the s for different values of u and a \\
*/

#include<stdio.h>

int
main(void)
{
    double TimeInSeconds[10];
    double Time, Distance, InitialSpeed, Acceleration;
    int i, i1, i2, i3;
    printf("Check distance for accelerating body every n seconds, where n = ");
    TimeInSeconds[0] = 0;
    scanf(" %lf", &TimeInSeconds[1]);
    for (i = 2; i <= 3; i++) {
        TimeInSeconds[i] = TimeInSeconds[(i-1)] + TimeInSeconds[1];
    }
    for (i1 = 0; i1 <= 2; i1++) {
        Time = TimeInSeconds[i1];
        printf("\n\n%d. At t = %.1lfs,\n\n\n", i1 + 1,  Time);
        for (i2 = 5; i2 <= 10; i2 += 5) {
            InitialSpeed = (double) i2/2;
            printf("\n\t%d. for u = %.1lfm/s\n\n", i2/5, InitialSpeed);
            for (i3 = 1; i3 <= 3; i3++) {
                Acceleration = (double) i3/10;
                printf("\t\t %d. for a = %.1lfm/(s*s) ", i3, Acceleration);
                Distance = (double) (InitialSpeed * Time) + ((Acceleration / 2) * (Time * Time));
                printf("Distance = %.5lfm\n", Distance);
            }
        }
    }
    return 0;
}