//todo 2. Write a program to print multiplication table of 10 in reversed order.


#include <stdio.h>

int main(){
    int n = 10;
    for(int i = 10; i<=n; i--){
        if(i==0){
            break;
        }
        printf("%d x %d = %d\n",n,i,n*i);
    }
    
    return 0;
}