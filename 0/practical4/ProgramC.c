#include<stdio.h>

int
main(void)
{
    int TimesTableOf, i;
    printf("Whose times table to see?\n");
    scanf("%d", &TimesTableOf);
    for(i = 1; i <= 10; i++)
        printf("%d * %d\t=\t%d\n", TimesTableOf, i, TimesTableOf * i);
    return 0;
}