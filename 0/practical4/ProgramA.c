/* Write a program to calculate the average of a set of N numbers. */

#include<stdio.h>
#include<stdlib.h>

int
main(void)
{
    int Numbers = 0, CurrentInput, i;
    int* Array = NULL;

    for (i = 0; i <= 25; i++) {
        printf("Enter a value. Enter a non-numerical value to calculate the average\n");

        if (scanf(" %d", &CurrentInput) == 1) {
            Numbers++;
            Array = realloc(Array, Numbers * sizeof(int));
            Array[i] = CurrentInput;
        }

        else
            break;
    }

    CurrentInput = 0;

    for (i = 0; i < Numbers; i++) {
        CurrentInput += Array[i];
    }

    if (Numbers > 0)   
    printf("Average of %i the numbers is %lf\n", Numbers, (double) CurrentInput/Numbers);

    else 
    printf("Nothing to do\n");
    
    free(Array);
    return 0;
}