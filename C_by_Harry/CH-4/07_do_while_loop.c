#include <stdio.h>

int main()
{
    int i = 0;

    do
    {
        printf("The value of i is : %d\n", i);
        i++; //this will only repeat if while condtion is true
    } while (i < 4);

    return 0;
}