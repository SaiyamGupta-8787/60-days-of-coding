#include <stdio.h>
//similar to boolean algebra, or = +, and = x, not = complement
int main(){
    int a=1; int b=1;
    printf("The value of a and b is %d\n",a&&b); //1 and 1
    printf("The value of a or b is %d\n",a||b); //1 or 1
    printf("The value of not(a) is %d\n",!a); //not 1

    // if(a){
    //     if(b){
              // printf("Both are true");
//          }
    //  }   
    // } ...Too long, too many indentations
    if(a && b){
        printf("Both are true\n");
    }

    int c=0; int d=1;
    printf("The value of c and d is %d\n",c&&d);
    printf("The value of c or d is %d\n",c||d);
    printf("The value of not(c) is %d\n",!c); //not 1

    int e=1; int f=0;
    printf("The value of e and f is %d\n",e&&f);
    printf("The value of e or f is %d\n",e||f);

    int g=0; int h=0;
    printf("The value of g and h is %d\n",g&&h);
    printf("The value of g or h is %d\n",g||h);

    return 0;
}