#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main(void) {
    double usd;
    system("clear");
    printf("Enter the number of U.S. Dollars you would like to convert\n");
    scanf("%lf",&usd);
    printf("The number of rupees is %.2lf\n", usd * 78.6);
    return 0;
}