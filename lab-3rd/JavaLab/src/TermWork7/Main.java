package TermWork7;

class PrimeTester implements IsPrime {
    @Override
    public boolean isPrime(int n) {
        boolean flag = true;
        for (int i = 2; i <= n - 1; i++) {
            if ((n % i) == 0) {
                flag = false;
                break;
            }
        }
        return flag;
    }
}

class ImprPrimeTester implements IsPrime {
    @Override
    public boolean isPrime(int n) {
        boolean flag = true;
        for (int i = 2; i <= n / 2; i++) {
            if ((n % i) == 0) {
                flag = false;
                break;
            }
        }
        return flag;
    }
}

class FasterPrimeTester implements IsPrime {
    @Override
    public boolean isPrime(int n) {
        boolean flag = true;
        for (int i = 2; i < Math.sqrt(n); i++) {
            if ((n % i) == 0) {
                flag = false;
                break;
            }
        }
        return flag;
    }
}

class FastestPrimeTester implements IsPrime {
    @Override
    public boolean isPrime(int n) {
        int a = 2;
        return Math.pow(a, n - 1) % n == 1;
    }
}

public class Main {
    public static void main(String[] args) {
        PrimeTester p1 = new PrimeTester();
        System.out.println("Using prime tester ");
        System.out.println("32 is Prime " + p1.isPrime(32));
        System.out.println("17 is Prime " + p1.isPrime(17));
        
        ImprPrimeTester p2 = new ImprPrimeTester();
        System.out.println("\nUsing ImprPrimeTester ");
        System.out.println("32 is Prime " + p2.isPrime(32));
        System.out.println("17 is Prime " + p2.isPrime(17));
       
        FasterPrimeTester p3 = new FasterPrimeTester();
        System.out.println("\nUsing Faster Prime Tester");
        System.out.println("32 is Prime " + p3.isPrime(32));
        System.out.println("17 is Prime " + p3.isPrime(17));
        
        FastestPrimeTester p4 = new FastestPrimeTester();
        System.out.println("\nUsing Fastest Prime Tester");
        System.out.println("32 is Prime " + p4.isPrime(32));
        System.out.println("17 is Prime " + p4.isPrime(17));

    }
}
