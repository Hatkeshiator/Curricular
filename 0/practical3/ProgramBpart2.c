#include<stdio.h>

int
main(void)
{
    int Input1,Input2,Input3,Input4;
    printf("Please enter four numbers.\n");
    scanf(" %d %d %d %d", &Input1, &Input2, &Input3, &Input4);
    printf("The ");
    if(Input1 > Input2 && Input1 > Input3 && Input1 > Input4) {
        printf("first");
    }
    else if(Input2 > Input1 && Input2 > Input3 && Input2 > Input4) {
        printf("second");
    }
    else if(Input3 > Input1 && Input3 > Input2 && Input3 > Input4) {
        printf("third");
    }
    else if(Input4 > Input1 && Input4 > Input2 && Input4 > Input3) {
        printf("fourth");
    }
    printf(" number is the greatest\n");
    return 0;
}