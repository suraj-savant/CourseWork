#include<stdio.h>

int main()
{
    int a, b, c;
    while(1)
    {
        
    printf("\nEnter the sides of tringle : ");
    scanf("%d%d%d", &a, &b, &c);

   if(a < (b+c) && b < (a+c) && c < (a+b) )
    {
        
        if(a==b && b==c)
            printf("The formed tringle is equilateral");
        else if(a !=b && b != c && a!=c)
            printf("Tringle is scalene");
        else 
            printf("Tringle is isosceles");   
        
    }
    else{
    printf("Tringle cannot formed");

    }
 
    }
   
}