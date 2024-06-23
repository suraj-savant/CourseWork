package Termwork5B;

public class Main {
    public static void main(String[] args) {
        
        double perimeter, area, volume;
        Cuboid cube = new Cuboid(10, 5, 3);
         perimeter =  cube.computePerimeter();
        area = cube.computerArea();
        volume = cube.computeVolume();
        System.out.println("Area, Perimeter and Volume of Cube : ");
        System.out.println("Perimeter : " + perimeter + " area : "  + area + " Volume : "+volume);
        
        Rectangle rect = new Rectangle(10, 5);
        perimeter = rect.computePerimeter();
        area = rect.computerArea();
        System.out.println("\nArea and perimeter of Rectangle : ");
        System.out.println("Perimeter : " + perimeter + " Area : "  + area );
    }
}