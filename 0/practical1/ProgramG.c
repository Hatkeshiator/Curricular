#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main(void) {
    double price_inr, price_paise;
    system("clear");
    printf("Please enter the INR price amount\n");
    scanf("%lf", &price_inr);
    price_paise = ceil(price_inr * 100);
    printf("The price in paise is %.0lf\n", price_paise);
    getchar();
    return 0;
}