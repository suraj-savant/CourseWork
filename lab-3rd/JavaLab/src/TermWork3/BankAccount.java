package TermWork3;

import java.util.Scanner;

public class BankAccount {

    int accountNumber;
    String name, address, accountType;
    double accBal;
    static int count = 0;

    Scanner sc = new Scanner(System.in);
    public BankAccount() {
       
        accountNumber = ++count;
         System.out.println("Enter the account holder name : ");
        name = sc.nextLine();
        System.out.println("Enter account holder address : ");
        address = sc.nextLine();
        System.out.println("Enter Account type : ");
        accountType = sc.nextLine();
        System.out.println("Enter the account balance : ");
        accBal = sc.nextDouble();  
    }

    public BankAccount(String name, String address, String accountType, double accBal) {
        this.accountNumber = ++count;
        this.name = name;
        this.address = address;
        this.accountType = accountType;
        this.accBal = accBal;
    }
    
    
    void computeInterest(int time){
        double interest = 0;
        if("SB".equals(this.accountType))
            interest = accBal * time * 5 / 100;
        else if("RD".equals(this.accountType)) 
            interest = accBal * time * 6.5 / 100;
        else if("FD".equals(this.accountType))
            interest = accBal * time * 7.65 /100;
        else 
            System.out.println("Invalid Account Type");
        System.out.println("The Interest is : "+ interest);
                    
    }
    
    
    void deposite(int amount){
        accBal += amount;
        System.out.println("Account Balance after deposite " + amount + " : " + accBal);
    }
    
    void withdraw(int amount){
        if(accBal - amount > 1000){
            accBal -= amount;
            System.out.println("After withdraw " + amount + " : " + accBal);
            return;
        }
        System.out.println("Insufficient balance withdraw of " + amount);
    }

    @Override
    public String toString() {
        return "\nName : " + name + "\nType " + accountType + "\n Balance " + accBal ;
    }

    
    
}
