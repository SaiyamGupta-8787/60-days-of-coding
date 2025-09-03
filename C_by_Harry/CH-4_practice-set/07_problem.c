//todo 7. Write a program to calculate the sum of the numbers occurring in the multiplication table of 8. (consider 8 x 1 to 8 x 10).


#include <stdio.h>

int main(){
    
    int n=8,s=0,i,m;
    for(i = 1; i<11;i++){
        m = n*i;
        s = s + m;
    }
    printf("Sum of multiples of 8 upto 10th multiple is = %d",s);

    return 0;
}