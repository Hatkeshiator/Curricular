#include<stdio.h>

int
main(void)
{
    int CheckEvenOdd;
    printf("Enter your number: ");
    scanf(" %d", &CheckEvenOdd);
    printf("The number %d is %s.\n", CheckEvenOdd, CheckEvenOdd % 2 == 0 ? "even" : "odd");
    return 0;
}