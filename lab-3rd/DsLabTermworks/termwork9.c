#include <stdio.h>
#include <stdlib.h>
#define MAX 10

void floyd(int W[][10], int n)
{
    int i, j, k;
    for (k = 1; k <= n; k++)
    {
        printf("\nMatrix D[%d]\n", k);
        for (i = 1; i <= n; i++)
        {
            for (j = 1; j <= n; j++)
            {
                if ((W[i][k] + W[k][j]) < W[i][j])
                    W[i][j] = W[i][k] + W[k][j];
                printf("%d\t", W[i][j]);
            }
            printf("\n");
        }
    }
}

int main()
{
    int i, j, n;
    int W[MAX][MAX];
    printf("Floyds Algorithm \n");
    printf("Enter number of nodes :");
    scanf("%d", &n);
    printf("\nEnter the edge weights :\n");
    for (i = 1; i <= n; i++)
        for (j = 1; j <= n; j++)
            scanf("%d", &W[i][j]);
    floyd(W, n);
    return 0;
}

// Input

// 0   999 3   999
// 2   0   999 999
// 999 7   0   1
// 6   999 999 0