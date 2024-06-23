package TermWork10;
import java.util.function.Predicate;  
 
 interface TaxCalculator {
    double calculateTax(double income);
}

public class Main {
    public static void main(String[] args) {
        TaxCalculator taxCalculator = (double income) -> {
            if (income <= 50000) {
                return income * 0.1;
            } else if (income > 50000 && income <= 100000) {
                return income * 0.2;
            } else {
                return income * 0.3;
            }
        };

        Predicate<Double> isTaxLessThan1000 = (tax) -> tax < 1000;

        double[] incomes = {9000,30000, 60000, 80000, 100000, 150000};
        for (double income : incomes) {
            double tax = taxCalculator.calculateTax(income);
            System.out.println("Income: " + income + ", Tax: " + tax + ", Less than 1000: " + isTaxLessThan1000.test(tax));
        }
    }
}
