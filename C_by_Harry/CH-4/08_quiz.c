#include <stdio.h>

int main()
{
    // todo : Write a program to print first ‘n’ natural number using do-while loop.

    int n_count, n_print = 1;
    printf("Enter number of natural numbers you want to print : ");
    scanf("%d", &n_count);
    do
    {
        printf("%d\n", n_print);
        n_print++;
    } while (n_print <= n_count);
    
    return 0;
}