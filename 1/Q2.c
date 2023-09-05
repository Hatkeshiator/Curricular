/*
*   initialize and use one of each of:
*   int, float, double, long, short, signed, unsigned, char
*   for a total of 6 unique variables.
*   print the age (in yrs) as int, height (in m) as float, weight (in kg) as
*   double, first letter of name (uppercase) as char, phone number as long, 
*   ZIP code as short, number of pets as unsigned, and difference between 
*   income and expenses (in USD) as signed.
*   age = 25
*   height = 1.75
*   initial = 'R'
*   weight = 65.5
*   phone no. = 9876543210
*   zipcode = 12345
*   pets = 2
*   bottom line = -500
*/

#include<stdio.h>

int
main(void)
{
    signed short int btmline = -500;
    unsigned short int zipcode = 12345, pets = 2, age = 25;
    unsigned long int number = 9876543210;
    float height = 1.750;
    double weight = 65.50;
    char initial = 'R';

    printf("What is the person's age in years?\n");
    scanf(" %hu", &age);

    printf("What is the person's height in meters?\n");
    scanf(" %f", &height);

    printf("What is the person's initial?\n");
    scanf(" %c", &initial);

    printf("What is the person's weight in kg?\n");
    scanf(" %lf", &weight);

    printf("What is the person's mobile number?\n");
    scanf(" %lu", &number);

    printf("What is the person's ZIP code?\n");
    scanf(" %hu", &zipcode);

    printf("How many pets does the person have?\n");
    scanf(" %hu", &pets);

    printf("What is the value (with minus sign if present) of the person's INCOME - their EXPENSES?\n");
    scanf(" %hd", &btmline);

    printf("The person's age is %hu years\n", age);
    printf("The person's height is %.2f meters\n", height);
    printf("The person's initial is %c\n", initial);
    printf("The person's weight is %.2lf kg\n", weight);
    printf("The person's phone number is %lu\n", number);
    printf("The person's ZIP code is %hu\n", zipcode);
    printf("The person owns %hu pets\n", pets);
    printf("The person's bottom line is $%hd\n", btmline);
    return 0;
}