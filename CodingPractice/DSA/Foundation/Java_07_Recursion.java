
public class Java_07_Recursion {
    static void fibo(){
        int num1 = 1; 
        int num2 = 1;
        for (int i = 0; i < 10; i++) {
            int fibo = num1 + num2;
            System.out.print(fibo + ", ");
            num1 = num2;
            num2 = fibo;
        }
        System.err.println();
    }
    public static void main(String[] args) {
        fibo();
    }

}

// public class Java_07_Recursion {
//     static int fact(int num) {
//         if (num == 1) {
//             System.out.println("1");
//             return 1;
//         }
//         System.out.print(num + " * ");
//         return num * fact(num - 1);
//     }

//     static int sum(int num) {
//         if (num == 1) {
//             System.out.println("1");
//             return 1;
//         }
//         System.out.print(num + " + ");
//         return num + sum(num - 1);
//     }

//     // Fibo nums : 1, 2, 3, 5, 8, 13
//     static int fibo(int num) {
//         if (num <= 1) {
//             return 1;
//         }
//         return fibo(num - 1) + fibo(num - 2);
//     }

//     public static void main(String[] args) {
//         // System.err.println("Recursive fact");
//         // System.out.println(fact(4));
//         // System.err.println("Recursive sum");
//         // System.out.println(sum(10));
//         for (int i = 0; i < 10; i++)
//             System.out.print(fibo(i) + ", ");
//         System.err.println();
//     }

// }


