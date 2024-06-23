package TermWork4;


public class Main {
    public static void main(String[] args) {
    FtEmploy ftEmployee1 = new FtEmploy("Kiran", "@Belagaum", "Male", 20, 20000);    
    FtEmploy ftEmployee2 = new FtEmploy("Ramesh", "@Belagaum", "Male", 25, 30000);
    ftEmployee1.calculateSalary();
    ftEmployee2.calculateSalary();
    System.out.println("\nDetils of full time employee :");
    ftEmployee1.show();
    ftEmployee2.show();
    
    PtEmployee ptEmployee1 = new PtEmployee("BE", 3, 20, "Ravi", "@Pune", "Male", 25);    
    PtEmployee ptEmployee2 = new PtEmployee("BE", 10, 30, "Sushant", "@Pune", "Male", 35);
    ptEmployee1.calculateSalary();
    ptEmployee2.calculateSalary();
    
    System.out.println("\nDetails of part time employee :");
    ptEmployee1.show();
    ptEmployee2.show();;
    
    }
    
}
