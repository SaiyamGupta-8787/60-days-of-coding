#include <stdio.h>

int main(){
    int i;
    for(i = 5 ; i ; i--){ //Will run until i = 0, because i being non zero is a true condition, this for loop will exit
        printf("%d\n",i);
    }
    return 0;
}