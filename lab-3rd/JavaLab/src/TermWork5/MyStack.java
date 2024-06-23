package TermWork5;

class MyStack {
    int[] elemt;
    int top;

    void initStack(int size) {
        elemt = new int[size];
        top = -1;
    }

    void initStack(MyStack stack) {
        elemt = new int[stack.elemt.length];
        top = -1;
        for (int i : stack.elemt) {
            push(i);
        }
    }
    
    void initStack(int[] elements){
        elemt = new int[elements.length];
        top = -1;
        for (int i : elements) {
            push(i);
        }
    }

    void push(int item){
        if(top < elemt.length){
            elemt[++top] = item;
            System.out.println("Push elemnt is " + item);
            return;
        }
        System.out.println("Stack is overflow");
    }

    int pop(){
        if (top == -1) {
            System.out.println("Stack is empty");
            return -1;
        }
        return elemt[top--];
    }

    int peak(){
        return elemt[top];
    }


    void display(){
        System.out.println("Stack elemnts are ");
     for (int i = top; i > -1; i--) {
        System.out.println(elemt[i]);
     }
    }

}