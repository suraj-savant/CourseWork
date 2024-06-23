// Binary Search
#include <stdio.h>
#include <time.h>

int Binary_Search(int A[], int k, int l, int h) // Binary Search code
{
    int m;
    while (l <= h)
    {
        m = (l + h) / 2;
        if (A[m] == k)
            return 1;
        else if (k > A[m])
            l = m + 1;
        else
            h = m - 1;
    }
    return 0;
}

int main()
{
    int A[1000], n, k, f = 0, i, j;
    clock_t s, e;
    double t;
    printf("\n Enter n value : ");
    scanf("%d", &n);

    for (i = 0; i < n; i++)
        A[i] = i;

    printf("\nArray Elements are : ");
    for (i = 0; i < n; i++)
        printf("%d ", A[i]);
    printf("\nEnter Key element : ");
    scanf("%d", &k);
    s = clock();
    for (i = 0; i < 10000; i++)
        for (j = 0; j < 10000; j++)
            f = Binary_Search(A, k, 0, n - 1);
    e = clock();
    t = (double)(e - s) / CLK_TCK;
    printf("Time taken = %lf", t);
    if (f == 1)
        printf("\nKey element found");
    else
        printf("\nKey element not found");
}
