#include <stdio.h>

int main()
{
    // int a;
    // a=1'
    int a = 1; // Takes 4 bytes( 1byte = 8-bits)

    // float b = 1.4;
    float b;
    b = 1.4; // Takes 4 bytes

    // char c ='a';
    char c;
    c = 'a'; // Always 1 byte
    printf("The value of a is %d\n",a);
    printf("The value of b is %f\n",b);
    printf("The value of c is %c\n",c);
} // Note: use sizeof(<datatype>) fxn to get size of datatype
