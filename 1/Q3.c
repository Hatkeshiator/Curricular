/*
*   program to take 5 digit input from user
*   and output reversed 5 digit number
*   and check if they're equal or not
*/

#include<stdio.h>

int
main(void)
{
    int input = 0, storedinput, i = 1, reversed = 0;
    printf("Enter the number you would like to invert\n");
    printf("Ensure that it is at most five digits in length. Invalid input will be handled with trailing 0's or truncation\n");
    
    scanf("%d", &input);
    storedinput = input;

    while (i <= 5)
    {
        reversed *= 10;
        reversed += input % 10;
        input /= 10;
        i++;
    }

    printf("Your number yields %d when reversed", reversed);

    if (reversed == storedinput) printf(", which is equal to your original number.\n");
    else printf(".\n");
    
    return 0;
}