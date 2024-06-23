// Infix Evaluation Using Stack
#include <stdio.h>
#include<stdlib.h>
#include<ctype.h>
#include<string.h>
#include<conio.h>
#include<math.h>

int numbers[50],tn=-1,to=-1;
char op[50];

void push_num(int n)
{
    numbers[++tn]=n;
}

void push_op(char ch)
{
    op[++to]=ch;
}

int pop_num()
{
    return numbers[tn--];
}

char pop_op()
{
    return op[to--];
}
int infix_eval(int numbers[50],char op[50]){
    int x,y;
    char ope;
    x=pop_num();
    y=pop_num();
    
    ope=pop_op();
    switch(ope)
    {
        case '+':
            return x+y;
        case '-':
            return y-x;
        case '*':
            return x*y;
        case '/':
            if(x==0)
            {
                printf("\nCannot divide by 0");
                exit(0);
            }
            else
                return y/x;
        case '^': return(pow(x,y));
    }
    return 0;
}
int is_operator(char ch)
{
    return (ch=='+' || ch=='-'||ch=='*'|| ch=='/'||ch=='^');
}

int precedence(char c)
{
    switch(c)
   {
        case '+':
            return 1;
        case '-':
            return 1;
        case '*':
            return 2;
        case '/':
            return 2;
        case '^':
            return 3;
    }
    return -1;
}

int eval(char expr[20])
{
    int i,num,output,r;
    char c;
    for(i=0;expr[i]!='\0';i++)
    {
        c=expr[i];
        if(isdigit(c)!=0)
        {
            num=0;
            while(isdigit(c))
           {
                num=num*10+(c-'0');
                i++;
                if(i<strlen(expr))
                {
                    c=expr[i];
                }
                else
                    break;
                
           }
            i--;
            push_num(num);
        }
        else if(c=='(')
            push_op(c);
        
        else if(c==')')
        {
            while(op[to]!='(')
            {
                r=infix_eval(numbers,op);
                push_num(r);
            }
            pop_op();
        }
        else if(is_operator(c))
        {
            while(to!=-1 && precedence(c)<=precedence(op[to]))
            {
                output=infix_eval(numbers,op);
                push_num(output);
            }
            push_op(c);
        }
    }
    while(to!=-1)
    {
        output=infix_eval(numbers,op);
        push_num(output);
    }
    return pop_num();
}


int main()
{
    char expr[50];
    printf("Enter the infix expression to evaluate: ");
    
    scanf("%s",expr);
    printf("%d",eval(expr));

    return 0;
}