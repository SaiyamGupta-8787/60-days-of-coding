// What will be the output of this program
// int a = 10;
// if (a = 11)
//  printf("I am 11");
// else
//  printf("I am not 11");

#include <stdio.h>

int main()
{
    int a = 10; //for single statement, we can use if else without'{}' also
    if (a = 11) // a is assigned 11, so non-zero value makes if statemet execute
        printf("I am 11");
    else
        printf("I am not 11");
    return 0;
}