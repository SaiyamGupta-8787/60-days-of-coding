//todo Write a program to find greatest of four numbers entered by the user
#include <stdio.h>

int main(){
    int a,b,c,d;
    printf("Enter a number : ");
    scanf("%d",&a);
    printf("Enter a number : ");
    scanf("%d",&b);
    printf("Enter a number : ");
    scanf("%d",&c);
    printf("Enter a number : ");
    scanf("%d",&d);

    // for a
    if(a==b && b==c && c==d){
        printf("All are equal");
    }
    else if(a>b && a>c && a>d){
        printf("%d is the greatest number",a);
    }
    else if(b>a && b>c && b>d){
        printf("%d is the greatest number",b);
    }
    else if(c>a && c>b && c>d){
        printf("%d is the greatest number",c);
    }
    else{
        printf("%d is the greatest number",d);
    }
    return 0;
}