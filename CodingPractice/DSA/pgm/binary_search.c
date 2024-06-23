#include<stdio.h>

int binary_search(int a[], int start, int end, int element)
{
  
    while(start <= end)
    {
        int mid = (start+end)/2;
        if(element == a[mid])
            return mid;
        else if(element < a[mid])
            end = mid -1;
        else
            start = mid + 1;            
    }
    return -1;
}


int main()
{
    int a[10];
    int size;
    int element;
    printf("Enter the size of array : ");
    scanf("%d", &size);

    printf("Enter the array elements : ");
    for(int i=0; i<size; i++)
        scanf("%d", &a[i]);

    while(1)
    {
        printf("\n\nEnter the search element : ");
        scanf("%d", &element);
        int index = binary_search(a,0,size,element);
        if(index == -1)
            printf("The search element not present");
        else
            printf("The search element present at index %d", index);
    }
    return 0;
}