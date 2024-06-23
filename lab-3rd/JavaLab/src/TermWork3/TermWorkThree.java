package TermWork3;

public class TermWorkThree {
    
    public static void main(String[] args) {
        BankAccount sb = new BankAccount();
        BankAccount rd = new BankAccount("Suraj", "At GIT Belagaum", "RD", 1000);
        BankAccount fd = new BankAccount();
        
        sb.deposite(1000);
        System.out.println(sb.toString());
        sb.withdraw(500);
        System.out.println(sb.toString());
        sb.deposite(2000);
        System.out.println(sb.toString());
        sb.withdraw(25000);
        System.out.println(sb.toString());
        
        rd.deposite(1000);
        System.out.println(rd.toString());
        rd.computeInterest(2);
        System.out.println(rd.toString());
      
        fd.deposite(1000);
        System.out.println(fd.toString());
        fd.computeInterest(2);
        System.out.println(fd.toString());
    }
}


