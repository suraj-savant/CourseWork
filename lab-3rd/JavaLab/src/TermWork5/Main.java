package TermWork5;

public class Main {
    public static void main(String[] args) {
        MyStack s1, s2;
        s1=new MyStack();
        s2 = new MyStack();
       
        System.out.println("\npush operation in s1");
        s1.initStack(3);
        s1.push(10);
        s1.push(20);
        s1.push(30);
        System.out.println("\ns1 stack elemnts are");
        s1.display();
       
        System.out.println("\npush operation in s2");
        s2.initStack(s1);   
        System.out.println("\ns2 stack elements are");
        s2.display();
       
        System.out.println("\npush in s2 using array");
        int[] elemt_array = {100, 200, 300, 400, 500};
        s2.initStack(elemt_array);

        System.out.println("\nPop elemt from s1 : " + s2.pop());
        System.out.println("Pop element form s2 : " + s2.pop());
        System.out.println("Peak of s2 : " + s2.peak());
        System.out.println("\ns2 stack elements are");
        s2.display();
    }
}