// todo FOR LOOP
// todo SYNTAX : for (initialize; test; increment or decrement)
// todo          {
// todo          //code.
// todo          }
//* initialize(only one time) -> test condition(everytime) -> execute //code. -> execute inc./dec., and will keep iterating until condtition stays true
#include <stdio.h>

int main()
{
    int n = 6;
    for (int i = 0; i < n; i++)
    {
        printf("The value of i is : %d\n", i);
    }
    return 0;
}