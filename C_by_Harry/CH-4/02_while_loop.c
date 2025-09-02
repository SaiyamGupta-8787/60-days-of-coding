#include <stdio.h>
//* While loop
int main()
{
    int i = 0;
    while (i < 5)
    { //* while loop iterates until conditon given remains true(non-zero vaue), then terminates
        printf("Happy Birthday!\n");
        i = i + 1; //* or use incrementing operator as i++;
    }



    return 0;
}