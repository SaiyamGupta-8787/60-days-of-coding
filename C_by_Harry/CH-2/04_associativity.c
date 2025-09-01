#include<stdio.h>

int main(){
    int a =3;
    int b = 6;
    int c = 9;

    printf("The value is %d",a*b/c);  //a*b first, then divide by c
    printf("The value is %d", 3*b/2*c +  7*a); //follow left to right
    // 3*b/2*c +  7*a
    // 3*b/2*c + 21
    // 18/2*c  + 21
    // 9*c + 21
    //81+21 = 102
    return 0;
}