package Termwork6;

public class Main {

    public static void main(String[] args) {
        Driver d1 = new Driver("Raju", 23, "Male");
        Car c1 = new MarutiCar("MyCar1", "CHI001", "CARMOD101");
        d1.driveCar(c1);

        Driver d2 = new Driver("Sham", 34, "Male");
        Car c2 = new BMWCar("MyCar2", "CHI983", "CARMOD345");
        d2.driveCar(c2);
    }
}
