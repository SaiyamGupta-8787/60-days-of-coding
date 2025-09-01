#include<stdio.h>

int main(){
    // '+' is used to add two numbers
    // '=' is the assignment operator
    int a = 4;
    int b = 3;
    int c = a + b;
    printf("The value of a is %d and value of b is %d and sum is %d",a,b,c);
    //'%'(Modulus) operator is used to get remainder
    printf("Remainder when a is divided by b is : %d\n",a%b);
    printf("%d", 3%11);
    //This does not work for exponentiation in c
    // int d = a^b; or a**b XXX
    return 0;
}