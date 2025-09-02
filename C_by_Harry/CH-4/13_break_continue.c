#include <stdio.h>

int main(){
    for(int i = 0; i<15;i++){
        if (i==11){
            break; //! EXIT THE LOOP NOW
             
        }
        else if(i==4){
            continue; //! SKIP THIS ITERATION/VALUE NOW
        }
        printf("i is %d\n",i);
    }
    printf("For loop is done");
    return 0;
}