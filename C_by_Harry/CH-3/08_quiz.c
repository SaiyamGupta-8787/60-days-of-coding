#include <stdio.h>

int main()
{
    /*
    Quick Quiz: Write a program to find grade of a student given his marks based on below:
        90 – 100 => A
        80 – 90 => B
        70 – 80 => C
        60 – 70 => D
        50 – 60 => E
        <50 => F
    */
    // 1st way
    //    int marks;
    //    printf("Enter your marks out of 100 : ");
    //    scanf("%d",&marks);

    //    if(marks<0 || marks>100){
    //     printf("Invalid");
    //    }
    //    else if(marks>90){
    //     printf("Grade is A");
    //    }
    //    else if(marks>80){
    //     printf("Grade is B");
    //    }
    //    else if(marks>70){
    //     printf("Grade is C");
    //    }
    //    else if(marks>=60){
    //     printf("Grade is D");
    //    }
    //    else if(marks>=50){
    //     printf("Grade is E");
    //    }
    //    else if(marks<50){
    //     printf("Grade is F");
    //    }

    //     return 0;
    // 2nd way
    char grade;
    int marks;
    printf("Enter your marks : ");
    scanf("%d", &marks);

    if(marks<0 || marks>100){
        printf("INVALID");
    }

    else if(marks <= 100 && marks >= 90)
    {
        grade = 'A';
    }
    else if ("marks<90 && marks>=80")
    {
        grade = 'B';
    }
    else if ("marks<80 && marks>=70")
    {
        grade = 'C';
    }
    else if ("marks<70 && marks>=60")
    {
        grade = 'D';
    }
    else if ("marks<60 && marks>=50")
    {
        grade = 'E';
    }
    else
    {
        grade = 'F';
    }
    printf("Grade is : %c",grade);
    return 0;
}