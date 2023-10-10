/*Given the values of the variables x, y and z, write a program
to rotate their values such that x has the value of y, y has the
value of z, and z has the value of x.*/

#include<stdio.h>

int
main(void)
{
    unsigned long long firstinput, secondinput, thirdinput, holder;

    printf("Enter the initial value of \"X\"\n");
    scanf(" %llu", &firstinput);
    printf("Enter the initial value of \"Y\"\n");
    scanf(" %llu", &secondinput);
    printf("Enter the initial value of \"Z\"\n");
    scanf(" %llu", &thirdinput);

    holder = firstinput;
    firstinput = secondinput;
    secondinput = thirdinput;
    thirdinput = holder;

    printf("After rotating, the values are:\nX =\t%llu\n", firstinput);
    printf("Y =\t%llu\n", secondinput);
    printf("Z =\t%llu\n", thirdinput);

    return 0;
}