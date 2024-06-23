
package Termwork6;

public class MarutiCar extends Car{

    MarutiCar(String carName, String chessiNum, String modelName) {
        super(carName, chessiNum, modelName);
    }

    @Override
    void startCar() {
        System.out.println("Maruti Car Started .....");   
    }

    @Override
    void operateStering() {
        System.out.println("Operate Stering of Maruti Car ...");     
    }

}
