#include<stdio.h>
//In C, all non-zero values are taken true

int main(){
    if(1){
        printf("This if is executed\n");
    }
    if(234){
        printf("This if is also executed\n");
    }
    if(2.34){
        printf("Executed\n");
    }
    if('c'){
        printf("Executed\n");
    }
    if(0){
        printf("Not executed\n");
    }
    return 0;
}