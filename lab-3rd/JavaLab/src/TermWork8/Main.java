package TermWork8;

import java.util.Scanner;

class UnderAgeException extends Exception{
    UnderAgeException(String s){
        super(s);
    }
    @Override
    public String toString(){
        return "Sorry. You are too young for the license";
    }
}
class ValidLLR extends Exception{
    ValidLLR(String s){
        super(s);
    }
    @Override
    public String toString(){
        return "Sorry. You do not hold a valid LLR";
    }
}
class NumAccidents extends Exception{
    NumAccidents(String s){
        super(s);
    }
    @Override
    public String toString(){
        return "Sorry. There are accidents in last one year";
    }
}
class License{
    String name;
    int age, no_of_cases;
    char gender;
    char validLLR;
    void readData(){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the name: ");
        name = sc.nextLine();
        System.out.println("Enter the age: ");
        age = sc.nextInt();
        System.out.println("Enter the gender: (M/F)");
        gender = sc.next().charAt(0);
        System.out.println("Do you have Valid LLR (Y/N)? ");
        validLLR = sc.next().charAt(0);
        System.out.println("How many number of cases in past one year? ");
        no_of_cases = sc.nextInt();
        sc.close();
    }
    
}

public class Main {
    public static void main(String[] args) {
        License applicant =new License();
        applicant.readData();
        validateApplicant(applicant);
    }

    static void validateApplicant(License a){
       try{
           if(a.age<18)
               throw new UnderAgeException("Underageexception:");
           if(a.validLLR!='Y')
               throw new ValidLLR("ValidLLRexception:");
           if(a.no_of_cases>0)
               throw new NumAccidents("Numberofaccidentsexception:");
           System.out.println("Congrats!! Your license is being posted");
       } 
       catch(UnderAgeException e){
           System.out.println(e.getMessage()+e);
       }
       catch(ValidLLR e){
           System.out.println(e.getMessage()+e);
       }
       catch(NumAccidents e){
           System.out.println(e.getMessage()+e);
       }
       catch(Exception e){
           System.out.println(e.getMessage()+e);
       }

    }
}
