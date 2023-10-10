#include<stdio.h>

int
main(void)
{
    int Input1, Input2, Input3, Input4;
    printf("Please enter the values.\n");
    scanf(" %d %d %d %d", &Input1, &Input2, &Input3, &Input4);
    printf("The ");
    if(Input1 > Input2){
        if(Input1 > Input3){
            if(Input1 > Input4){
                printf("first");
            }
            else{
                printf("fourth");
            }
        }
        else{
            if(Input3 > Input4){
                printf("third");
            }
            else{
                printf("fourth");
            }
        }
    }
    else{
        if(Input2 > Input3){
            if(Input2 > Input4){
                printf("second");
            }
            else{
                printf("fourth");
            }
        }
        else{
            if(Input3 > Input4){
                printf("third");
            }
            else{
                printf("fourth");
            }
        }
    }
    printf(" number is the greatest\n");
    return 0;
}