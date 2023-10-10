#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main(void) {
    double princ, rate, timeus, amt_after;
    system("clear");
    printf("What is your starting amount (principal)?\n");
    scanf("%lf", &princ);
    princ = round(princ * 100) / 100; //rounds off princ to 2 dec places; %.2lf is not valid for scanf
    printf("What is the rate of interest in percentages? e.g. 7.5\n");
    scanf("%lf", &rate);
    printf("How many units of time has your principal been collecting interest?\ne.g. months for monthly interest, years for annual\n");
    scanf("%lf", &timeus);
    timeus = floor(timeus);
    amt_after = princ;
    princ = princ * rate * timeus / 100;
    amt_after = amt_after + princ;
    printf("Your final interested amount is %.2lf\n", amt_after);
    getchar();
    return 0;
}