//todo 10. Write a program to check whether a given number is prime or not using loops.

#include <stdio.h>

int main(){
    
    int n;
    printf("Enter a number : ");
    scanf("%d",&n);
     int prime=0;
     for (int  divisor = 2; divisor < n; divisor++)
     {
        if(n%divisor==0){
            prime = 1;
            break;
        }
     }
     if(prime){
        printf("NOT PRIME\n");

     }
     else{
        printf("PRIME");
     }

    return 0;
}