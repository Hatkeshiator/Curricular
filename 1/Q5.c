/*
*   Check whether a character is upper- or lower-case
*   Also check consonant or vowel
*/

#include<stdio.h>

int
main(void)
{
    char input;
    
    printf("Please enter your character: ");
    scanf("%c", &input);

    printf("Your character is a ");
    input >= 'a' && input <= 'z' ? printf("lowercase ") : printf("uppercase ");
    input == 'a' || input == 'A' || input == 'e' || input == 'E' || input == 'i' || input == 'I' || input == 'o' || input == 'O' || input == 'u' || input == 'U' ? printf("vowel.\n") : printf("consonant.\n");

    return 0;
}