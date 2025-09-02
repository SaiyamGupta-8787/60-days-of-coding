#include <stdio.h>

int main(){
    int i = 5;
    printf("the value of i is : %d\n",i);
    i = i + 5; // i = 10
    printf("the value of i is : %d\n",i);
    printf("the value of i is : %d\n",i++); //i = 11 after printing
    ++i; //i=12
    printf("the value of i is : %d\n",i);

    //! i++; prints first and then increments, knowns as post increment operator
    //! ++i; increments first and then prints, known as pre increment operator

    //i = i + 2;//Adding 2 to i, i = 14
    i+=2; //compound assignment operator,same as above, and also works for all other operators 
    return 0;
}