#include <stdio.h>

int main()
{

    int i = 0;
    while (i < 10) //or while(1<10){}
    {
        printf("the value of i is : %d\n", i); //program will never stop, as condition remains infintely true, do not run on laptop as can casue heating or temporary problems and even permanent problems
    }
    return 0;
}