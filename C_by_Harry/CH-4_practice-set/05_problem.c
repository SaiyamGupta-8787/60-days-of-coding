//todo 5. Write a program to sum first ten natural numbers using while loop.

#include <stdio.h>

int main(){
    int n = 10,s=0;
    for(int i = 1; i<(n+1); i++ ){
        s = s + i;
    }
    printf("the sum of first 10 natural numbers is = %d",s);
    return 0;
}