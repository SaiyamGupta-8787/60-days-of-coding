#include<stdio.h>

int main(){
    float a = 9.0;
    int b = 2;
    float c = a/b;
    int d = 6.7;
    printf("The value of a/b is %f\n",c);
    printf("The value of d is %d",d); //Float 6.7 is demoted to 6 as data type is int, so type compatibility is important
    return 0;
}