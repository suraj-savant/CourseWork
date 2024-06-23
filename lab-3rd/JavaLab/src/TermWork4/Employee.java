package TermWork4;


public class Employee {

    String name, address, gender;
    int age;
    double salary;

    Employee(String name, String address, String gender, int age) {
        this.name = name;
        this.address = address;
        this.gender = gender;
        this.age = age;
    }

    void show() {
        System.out.println("\nName : " + name + "\nAddress : " + address + "\nGender : " + gender + "\nAge : " + age + "\nSalary : " + salary);
    }

}

class FtEmploy extends Employee {

    double baseSalary;

     FtEmploy( String name, String address, String gender, int age, double baseSalary) {
        super(name, address, gender, age);
        this.baseSalary = baseSalary;
    }

    void calculateSalary() {
        salary = baseSalary + baseSalary * 0.75 + baseSalary * 0.075 + baseSalary * 0.1;
    }
}

class PtEmployee extends Employee {

    String qualification;
    int experience, numberOfHours;

     PtEmployee(String qualification, int experience, int numberOfHours, String name, String address, String gender, int age) {
        super(name, address, gender, age);
        this.qualification = qualification;
        this.experience = experience;
        this.numberOfHours = numberOfHours;
    }

    void calculateSalary() {
        double netSalary = 0;
        switch (qualification) {
            case "BE":
                if (experience <= 5) {
                    netSalary = numberOfHours * 300;
                } else if (experience <= 10) {
                    netSalary = numberOfHours * 400;
                } else {
                    netSalary = numberOfHours * 1000;
                }
                break;
            case "MTECH" :
                   if (experience <= 5) {
                    netSalary = numberOfHours * 500;
                } else if (experience <= 10) {
                    netSalary = numberOfHours * 700;
                } else {
                    netSalary = numberOfHours * 1000;
                }
                break;
             case "PHD" :
                   if (experience <= 5) {
                    netSalary = numberOfHours * 800;
                } else if (experience <= 10) {
                    netSalary = numberOfHours * 1200;
                } else {
                    netSalary = numberOfHours * 1500;
                }
                break;  
             default:
                 System.out.println("Invalid qualification");
        }
        super.salary = netSalary;
    }
}

