
package Termwork6;
abstract class Car {
    String carName, chessiNum, modelName;

    public Car(String carName, String chessiNum, String modelName) {
        this.carName = carName;
        this.chessiNum = chessiNum;
        this.modelName = modelName;
    }
    
    abstract void startCar();
    abstract void operateStering();
    
    void display(){
        System.out.println("\nCar details : ");
        System.out.println("Car Name : "+ carName + "\nChessi Number : " + chessiNum + "\nModel Name : " + modelName);
    }
}
