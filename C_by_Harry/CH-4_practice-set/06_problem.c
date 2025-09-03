//todo 6. Write a program to implement program 5 using ‘while’ and ‘do-while’ loop.


#include <stdio.h>

int main(){
    //todo using while loop
    int n=10,s=0,i=1;
    while(i<(n+1)){
        s+=i;
        i++;
    }
    printf("The sum of first ten natural nos is = %d\n",s);
    int a=10,b=0,c=1;
    do{
        b = b + c;
        c++;
    }while(c<(a+1));
    printf("The sum of first ten natural nos is = %d",b);

    return 0;
}