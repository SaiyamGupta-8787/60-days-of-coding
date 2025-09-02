//todo Write a program to print first ‘n’ natural numbers using for loop
#include <stdio.h>

int main(){
    int n_count;
    printf("Enter the number of natural nos you want to print : ");
    scanf("%d",&n_count);

    for(int n_print=1; n_print<=n_count;n_print++){
        printf("%d\n",n_print);
    }
    return 0;
}