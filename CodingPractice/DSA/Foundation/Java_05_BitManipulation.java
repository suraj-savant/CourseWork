package Foundation;

public  class Java_05_BitManipulation {
    public static void main(String[] args) {
        int num = 10;
// Convert int to Binary
        String binary  = Integer.toBinaryString(num);
        System.out.println("Num to binary " + binary);

//  Convert Binary to Int
        int numFromBinary = Integer.parseInt(binary, 2);
        System.out.println("num from binary " + numFromBinary);
    }
}


//
//public class Java_05_BitManipulation {
//
//        // Method to check if a number is even or odd using bitwise AND
//        public static boolean isEven(int n) {
//            return (n & 1) == 0;
//        }
//
//        // Method to swap two numbers using XOR
//        public static void swapNumbers(int a, int b) {
//            System.out.println("Before swap: a = " + a + ", b = " + b);
//            a = a ^ b;
//            b = a ^ b;
//            a = a ^ b;
//            System.out.println("After swap: a = " + a + ", b = " + b);
//        }
//
//        // Method to count the number of set bits (1s) in an integer
//        public static int countSetBits(int n) {
//            int count = 0;
//            while (n > 0) {
//                count += (n & 1);
//                n >>= 1;
//            }
//            return count;
//        }
//
//        // Method to check if a number is a power of two
//        public static boolean isPowerOfTwo(int n) {
//            return n > 0 && (n & (n - 1)) == 0;
//        }
//
//        // Method to find the single number in an array where every element appears twice except for one
//        public static int findSingleNumber(int[] nums) {
//            int result = 0;
//            for (int num : nums) {
//                result ^= num;
//            }
//            return result;
//        }
//
//        public static void main(String[] args) {
//            // Demonstrate isEven
//            int num1 = 4;
//            int num2 = 7;
//            System.out.println(num1 + " is even: " + isEven(num1));
//            System.out.println(num2 + " is even: " + isEven(num2));
//
//            // Demonstrate swapNumbers
//            swapNumbers(3, 4);
//
//            // Demonstrate countSetBits
//            int num3 = 15; // binary: 1111
//            System.out.println("Number of set bits in " + num3 + ": " + countSetBits(num3));
//
//            // Demonstrate isPowerOfTwo
//            int num4 = 16;
//            int num5 = 18;
//            System.out.println(num4 + " is power of two: " + isPowerOfTwo(num4));
//            System.out.println(num5 + " is power of two: " + isPowerOfTwo(num5));
//
//            // Demonstrate findSingleNumber
//            int[] nums = {4, 1, 2, 1, 2};
//            System.out.println("The single number in the array is: " + findSingleNumber(nums));
//        }
//    }
//
//
//
//
