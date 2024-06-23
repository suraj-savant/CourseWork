#include <stdio.h>
#include <stdlib.h>
#include<time.h>

#define MAX 20000

int A[MAX];

void Quicksort( int low , int high);
int Partition(int low , int high);
void swap(int *p , int *q);

int main()
{
    int n,i,j;
    int low , high;

    clock_t s , e ;
    double  cpu_exe_t;

    printf("\nPlease enter the size of the array :");
    scanf("%d",&n);
// Random order
printf("The array elements ran are : \n");
    for(i=0;i<n;i++)
    {
        A[i]=rand()%100; /*scanf("%d",&A[i]);*/
    }

// Asending order
    printf("\nThe array elements asc are :\n");
    for(i=0;i<n;i++)
    {
        printf("%d\t",A[i] = i+1);
    }

// Desending order
 printf("\nThe array elements desc are :\n");
    int temp = n;
    
    for(i=0;i<n;i++)
    {
        printf("%d\t",A[i] = temp--);
    }
    

    s=clock();
    for(j=0;j<1000;j++)            //Delay loops
    for(i=0;i<1000;i++)
    {
        low=0;
        high=n-1;
        Quicksort(low,high);
    }
    e=clock();

    cpu_exe_t=(double)(e-s)/CLK_TCK;

    printf("\nThe sorted array is :\n");
    for(i=0;i<n;i++)
    {
        printf("%d\t",A[i]);
    }

    printf("\nCPU execution time is %lf",cpu_exe_t);

    return 0;
}

int Partition( int low , int high)
{
    int i,j;
    int pivot=A[low];

    i=low;
    j=high+1;

    while(i<j)
    {
        do
        {
            ++i;
        }while(A[i]<=pivot);

        do
        {
            --j;
        }while(A[j]>pivot);

        if(i<j)
        {
           swap(&A[i],&A[j]);
         
        }
    }

    swap(&A[low],&A[j]);


    return j;
}

void Quicksort( int low , int high)
{
    int j;

    if(low<high)
    {
        j=Partition(low,high);
        Quicksort(low , j-1);
        Quicksort(j+1 , high);
    }
}

void swap(int  *a , int   *b)
{
    int t;
    t= *a;
    *a=*b;
    *b=t;
}


