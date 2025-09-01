// Write a C program to calculate area  of a rectangle using
// a)Hard coded inputs
// b)Using Inputs Supplied by user
#include <stdio.h>

int main(){
    // int l = 3, b = 6;
    int length,breadth;
    printf("Enter Length : ");
    scanf("%d",&length);
    printf("Enter Breadth : ");
    scanf("%d",&breadth);    
    printf("Area of rectangle is  : %d",length*breadth);
    return 0;
}