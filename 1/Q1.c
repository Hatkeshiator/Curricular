/*
*   use data types int, float, char and double.
*   print store bill with int = 5 items, float = 0.07 tax rate, char = $ double = 23.45 subtotal (pre-tax)
*   calculate and print double = price after tax
*/

#include<stdio.h>

int
main(void)
{
    int items = 5;
    float tax_rate = 0.07;
    char currency_symbol = '$';
    double subtotal = 23.45, total;

    printf("Items bought: ");
    scanf(" %d", &items);
    
    printf("Tax rate (1%% -> 0.01): ");
    scanf(" %f", &tax_rate);
    
    printf("Currency: ");
    scanf(" %c", &currency_symbol);
    
    subtotal = (double) items * 4.69;
    total = subtotal + (subtotal * tax_rate);
    printf("Number of items:\t%d\nTax rate:\t\t%.0f%%\nSubtotal:\t\t%c%.2lf\nTotal:\t\t\t%c%.2lf\n", items, tax_rate * 100, currency_symbol, subtotal, currency_symbol, total);
    return 0;
}   