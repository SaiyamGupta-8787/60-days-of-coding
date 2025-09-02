#include <stdio.h>

int main()
{
    // todo Write a program to find whether a year input by the user is leap year or not
    int year;
    printf("Enter year : \n");
    scanf("%d", &year);
    if(year<1){
        printf("year cannot be less than 1");
    }
    else if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) //* leap year must be divisible by both 4 and 100
    {
        printf("This is a leap year");
    }
    else
    {
        printf("Not a leap year");
    }

    return 0;
}