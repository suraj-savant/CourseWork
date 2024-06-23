// Queue application
#include<stdio.h>
#define size 5

int queue[5], front = 0, rear = -1;

void enqueue()
{
    int data;
    printf("Enter the data to be inserted : ");
    scanf("%d", &data);
    if( rear == size - 1 )
    {
        printf("\nQueue is full");
        return;
    }
    queue[++rear] = data;
}

void dequeue()
{
    if (rear < front)
    {
        printf("\nQueue is empty");
        return;
    }
        printf("\nThe removed element is %d\n", queue[front++]);
    
}

void display()
{
    if(rear < front)
    {
        printf("\nQueue is empty");
        return;
    }
    printf("\nQueue elemts are : \n");
    for (int i = front; i <= rear; i++)
    {
        printf("%d\t", queue[i]);
    }
    
}

int main(int argc, char const *argv[])
{
     int choice;
    while (1)
    {
        printf("\n\n(1)Enqueue\n(2)Dequeue\n(3)Display\n(0)EXIT");
        printf("\nEnter your choice : ");
        scanf("%d", &choice);
        switch (choice)
        {
        case 0:
            return 0;
        case 1:
            enqueue();
            break;
        case 2:
            dequeue();
            break;
        case 3:
            display();
            break;       

        default:
            printf("\nInvalid option");
            break;
        }
    }
    return 0;
}
