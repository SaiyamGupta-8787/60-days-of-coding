#include <stdio.h>

int main(){
    int i,n;
    printf("Enter number of natural nos to be printed : ");
    scanf("%d",&n);

    for(i=n;i;i--){
        printf("%d\n",i);
    }
    return 0;
}