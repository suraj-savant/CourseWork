
package Termwork6;

public class Driver {
  String name, gender;
  int age;

    public Driver(String name, int age, String gender) {
        this.name = name;
        this.age = age;
        this.gender = gender;
    }
  
  void driveCar(Car car){
      driverInfo();
      car.display();
  }
  
   void driverInfo(){
      System.out.println("\nDriver Info");
      System.out.println("Name : " + name);
      System.out.println("Age : " + age);
      System.out.println("Gender : " + gender);
  } 
}
