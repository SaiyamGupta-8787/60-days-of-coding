#include <stdio.h>

int main()
{
    int income;
    float tax = 0;

    printf("Enter Annual Income: ");
    scanf("%d", &income);

    if (income <= 250000) {
        tax = 0; //taxable income = 0
    }
    else if (income <= 500000) {
        tax = 0.05 * (income - 250000); //taxable income = (income - 2.5L) at 5% rate
    }
    else if (income <= 1000000) {
        tax = 0.05 * (500000 - 250000)+ 0.20 * (income - 500000);
    }
    else {
        tax = 0.05 * (500000 - 250000) + 0.20 * (1000000 - 500000) + 0.30 * (income - 1000000); 
    }

    printf("The total tax you have to pay is %.2f\n", tax); //.2f means only upto 2 decimal places

    return 0;
}
