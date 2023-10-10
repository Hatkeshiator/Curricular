#include<stdio.h>

int
main(void)
{
    int i, count = 0;
    for(i = 1; i <= 100; i++) {
        if (i % 6 == 0 && i % 4 != 0) {
            printf("%d\n", i);
            count++;
        }
    }
    printf("total is %d\n", count);
    return 0;
}