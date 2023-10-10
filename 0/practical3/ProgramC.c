#include<stdio.h>

int
main(void)
{
    int MathMarks, PhysMarks, ChemMarks;
    int i;
    printf("Enter your marks in ");
    for(i = 1; i <= 3; i++) {
        switch(i){
            case 1:
                printf("Math: ");
                break;
            case 2:
                printf("Physics: ");
                break;
            case 3:
                printf("Chemistry: ");
                break;
            default:
                break;
        }
        scanf(" %d", i == 1 ? &MathMarks : (i == 2 ? &PhysMarks : &ChemMarks));
    }
    if (MathMarks >= 60 && PhysMarks >= 50 && ChemMarks >= 40) {
        if(MathMarks + PhysMarks + ChemMarks >= 200 || MathMarks + PhysMarks >= 150) {
            printf("You were accepted!\n");
        }
        else {
            printf("You were rejected.\n");
        }
    }
    else{
        printf("You were rejected.\n");
    }
    return 0;
}