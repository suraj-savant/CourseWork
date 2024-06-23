
package TermWork2;
import java.util.Scanner;
import static java.lang.System.exit;

public class MyTringle {
    double side1,side2,side3;
    public static void main(String[] args) {
        MyTringle tringle = new MyTringle();
        tringle.getSides();
        tringle.checkType();
        System.out.println("Area of tringle " + tringle.computeArea());
    }
  
    void getSides()
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter sides of tringle");
        side1 = sc.nextDouble();
        side2 = sc.nextDouble();
        side3 = sc.nextDouble();
        sc.close();
    }

    void checkType()
    {
        if ((side1+side2)> side3 && (side1+side3) > side2 && (side2+side3) > side1 ) {
            if(side1==side2 && side2==side3){
                System.out.println("Tringle is Equilateralquilateral");
            }
            else if (side1==side2 || side2==side3 || side1==side3) {
                System.out.println("Tringle is Isosceles");
            }
            else{
                System.out.println("Tringle is Scalene");
            }
        }
        else{
            System.out.println("Tringle cannot be formed");
            exit(0);
        }

    }

    double computeArea(){
        double s, area;
         s = (side1+side2+side3)/2;
         area = Math.sqrt(s * (s-side1) * (s-side2) * (s-side3));
         return area;
    }

  
}
