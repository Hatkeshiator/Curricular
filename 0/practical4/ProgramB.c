/* Write a program to count all the prime numbers that lie between 100 and 200. */

#include <stdio.h>
#include <math.h>

int
main(void)
{
    unsigned long long int i, i2, primes = 0;
    
    for (i = 100; i <= 200; i++) {
        int isPrime = 1;
        
        for (i2 = 2; i2 <= sqrt(i); i2++) {
            if (i % i2 == 0) {
                isPrime = 0;
                break;
            }
        }
        
        if (isPrime) {
            printf("%llu is prime\n", i);
            primes++;
        }
    }
    
    printf("\nThus there are %llu prime numbers between 100 and 200\n", primes);
    return 0;
}