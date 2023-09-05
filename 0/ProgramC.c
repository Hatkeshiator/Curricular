#include<stdio.h>
#include<stdlib.h>

int main(void) {
    int hoursi, minsi, hourso, minso;
    system("clear");
    printf("Enter number of hours\n");
    scanf("%d",&hoursi);
    printf("Enter number of minutes\n"); 
    scanf("%d",&minsi);
    hourso = hoursi + (minsi / 60);
    minso = minsi + (hoursi * 60);
    printf("Your desired time in hours is %d with %d minutes left over\nYour desired time in minutes is %d\n", hourso, minsi % 60, minso);
    getchar();
    return 0;
}