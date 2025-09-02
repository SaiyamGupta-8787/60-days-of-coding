#include <stdio.h>

int main(){
    int age = 48;
//if ,else if, and else ladder
    if(age>60){
        printf("You can drive and you are a senior citizen"); //if true, then program ignore all condition written below it if they are 'else if'
    }
    else if(age>40){
        printf("You can drive and you are an elder"); //we can take any no. of else if, but ony one if and one else are allowed in a single ladder
    }
    else if(age>18){
        printf("You can drive");  //same as elif in python
    }
    else{
        printf("You cannot drive"); //optional, w can just write else if only
    }
    return 0;
}