#include <stdio.h>

int main()
{
    // Write a program to determine whether a student has passed or failed. To pass, a
    //  student requires a total of 40% and at least 33% in each subject. Assume there
    //  are three subjects and take the marks as input from the user.
    int m1, m2, m3;
    // int value_of_marks; //write only vom, then hit enter,vscode automatically makes correct longer name
    printf("Enter marks of 1st subject : \n");
    scanf("%d", &m1);
    printf("Enter marks of 2nd subject : \n");
    scanf("%d", &m2);
    printf("Enter marks of 3rd subject : \n");
    scanf("%d", &m3);

    if (m1 < 33 || m2 < 33 || m3 < 33)
    {
        printf("You are failed due to less than 33 marks in individual subject(s)\n");
    }
    else if ((m1 + m2 + m3) / 3 < 40)
    {
        printf("You are failed as your average marks are less than 40% \n");
    }
    else{
        printf("You are passed\n");
    }
    return 0;
}