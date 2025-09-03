//todo 8. Write a program to calculate the factorial of a given number using a for loop.

#include <stdio.h>
//! Factorial, n! = n x (n-1) x (n-2) x (n-3)... x 3 x 2 x 1
int main(){
    int n,factorial=1; //*in most of the cases, prod.=1, sum.=0
    printf("Enter a number : ");
    scanf("%d",&n);

    for(int i = 1; i<=n; i++){
        factorial = factorial*i;
    }
    
    printf("The factorial of %d is = %d\n", n , factorial);
    return 0;
}