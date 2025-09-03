//todo 9. Repeat 8 using while loop.

#include <stdio.h>

int main(){
                                                               
    int n,f=1;                           //!OR           // int i = 1;       
    int m = n;                                           // int product = 1;   
    printf("Enter a number : ");                         // int n;
    scanf("%d",&n);                                      // printf("enter a number : ");           
    while(1){                                            // scanf("%d",&n);             
        if(n==0){                                        // while(i<=n){         
            break;                                       //     product *= i;      
        }                                                //     i++; 
        f = f*n;                                         // }    
        n--;                                             // printf("The factorial of %d is = %d\n",n,product);              
    }
    printf("The factorial of %d is = %d\n",m,f);                                      

    return 0;                                                                   
}

// int i = 1;
// int product = 1;
// int n;
// printf("enter a number : ");
// scanf("%d",&n);
// while(i<=n){
//     product *= i;
//     i++;
// }
// printf("The factorial of %d is = %d\n",n,product);