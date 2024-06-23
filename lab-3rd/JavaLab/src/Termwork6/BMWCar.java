package Termwork6;

public class BMWCar extends Car{

    BMWCar(String carName, String chessiNum, String modelName) {
        super(carName, chessiNum, modelName);
    }

    @Override
    void startCar() {
        System.out.println("BMW Car Started .....");   
    }

    @Override
    void operateStering() {
        System.out.println("Operate Stering of BMW Car ...");     
    }

}