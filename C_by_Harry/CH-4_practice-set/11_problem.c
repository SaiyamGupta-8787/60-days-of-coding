// todo 11. Implement 10 using other types of loops.
// WITH WHIILE LOOP
// #include <stdio.h>

// int main() //go down for do while
// {
//     int n, i = 2, isPrime = 1;
//     printf("enter a number : ");
//     scanf("%d", &n);

//     if (n <= 1)
//     {
//         isPrime = 0;
//     }
//     else
//     {
//         while (i < n)
//         {
//             if (n % i == 0)
//             {
//                 isPrime = 0;
//                 break;
//             }
//             i++;
//         }
//     }

//     if (isPrime)
//     {
//         printf("Prime\n");
//     }
//     else
//     {
//         printf("Not prime\n");
//     }

//     return 0;
// }
// WITH DO WHILE LOOP
#include <stdio.h>

int main()
{
    int n, i = 2;
    printf("Enter a number : ");
    scanf("%d", &n);
    int prime = 1;
    if (n <= 1)
    {
        prime = 0;
    }
    else
    {
        do
        {
            if (n % i == 0)
            {
                prime = 0;
                break;
            }
            i++;
        } while (i < n);

        if(prime){
            printf("Prime");
        }
        else{
            printf("Not prime");
        }
    }
    
    return 0;
}