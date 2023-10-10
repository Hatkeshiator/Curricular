#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main(void) {
    double price_kg = 16.75;
    double psugar_kg = 15;
    double qrice, qsugar;
    system("clear");
    printf("The price of rice (or pRICE, as it were) is 16.75 INR/kg while that of sugar is 15 INR/kg.\nHow many kg of each do you want to buy?\n");
    scanf("%lf%lf",&qrice,&qsugar);
    printf("ITEM\t\tQTY\t\tCOST\nRCE.\t\t%3.0lf\t\t%7.2lf\nSGR.\t\t%3.0lf\t\t%7.2lf\nTOTL\t\t\t\t%7.2lf\n",round(qrice),ceil(round(qrice)*price_kg),round(qsugar),ceil(round(qsugar)*psugar_kg),(ceil(round(qsugar)*psugar_kg))+(ceil(round(qrice)*price_kg)));
    getchar();
    return 0;
}