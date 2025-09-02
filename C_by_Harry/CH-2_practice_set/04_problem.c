#include<stdio.h>

int main(){
    //Explain step by step evaulation of 3*x/y - z+k,where x=2, y=3, z=3, k=1
    int x =2,y=3,z=3,k=1;
    float exp = 3*x/y - z+k;
    // 3*x/y - z+k
    // 6/y - z+k
    // 2 - z+k
    // -1+k = -1 + 1 = 0
    printf("The value of expression is = %f",exp);
    return 0;
}