#include <stdio.h>

int main(){
    //todo Quiz: Write a program to print natural numbers from 10 to 20 when initial loop counter is initialized to 0.  The loop counter need not be int, it can be float as well

    int i = 0; //* i is loop counter
    while(i<=20){
        if(i>=10){
            printf("The value of i is : %d\n",i);
        }
        i++;
    }
    return 0;
}