// Binary Tree

#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node *left, *right;
};

struct node *head = NULL;

void insert(int a)
{
    struct node *temp = (struct node *)malloc(sizeof(struct node));
    struct node *curr = head;
    struct node *prev = NULL;
    temp->data = a;
    temp->left = NULL;
    temp->right = NULL;
    if (head == NULL)
    {
        head = temp;
        return;
    }
    while (curr != NULL)
    {
        prev = curr;
        if (a > curr->data)
            curr = curr->right;
        else
            curr = curr->left;
    }
    if (a >= prev->data)
        prev->right = temp;
    else
        prev->left = temp;
}

void inorder(struct node *n)
{
    if (n != NULL)
    {
        inorder(n->left);
        printf("%d ", n->data);
        inorder(n->right);
    }
}

void preorder(struct node *n)
{
    if (n != NULL)
    {
        printf("%d ", n->data);
        preorder(n->left);
        preorder(n->right);
    }
}

void postorder(struct node *n)
{
    if (n != NULL)
    {
        postorder(n->left);
        postorder(n->right);
        printf("%d ", n->data);
    }
}

int main()
{
    int a, ch, n;
 
        printf("Enter the number of elements : ");
        scanf("%d", &n);
        for (int i = 0; i < n; i++)
        {
            printf("Enter %d tree element : ", i+1);
            scanf("%d", &a);
            insert(a);
        }
        
    printf("Inorder\n");
    inorder(head);
    printf("\nPreorder\n");
    preorder(head);
    printf("\nPostorder\n");
    postorder(head);
}