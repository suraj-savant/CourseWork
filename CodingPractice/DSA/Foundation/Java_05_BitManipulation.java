
public class Java_05_BitManipulation {

    static int toInteger(String binary){
        int integer = 0;
        int end =  binary.length()-1;        
        for (int i = end; i >= 0; i--) {
            int radix = end -i;
            int base =Integer.parseInt(binary.substring(i, i+1));
            integer += Math.pow(base, radix);
            
        }

        return integer;
    }

    static String toBinary(int num){
        String binary = "";
        while(num != 0){
            int digit = num % 2;
            binary = digit + binary;
            num /= 2;

        }
        return binary;
    }
    public static void main(String[] args) {
       int i =  toInteger("1111");
       System.out.println(i);
        // System.out.println(toBinary(10));
    }
    
}


// public class Java_05_BitManipulation {

//     static String intTOBinary(int num) {

//         // Convert int to Binary
//         String binary = Integer.toBinaryString(num);
//         return binary;
//     }

//     static int binaryToInt(String binary) {

//         //  Convert Binary to Int
//         int num = Integer.parseInt(binary, 2);
//         return  num;

//     }

//     static int countBits(int num) {

//         int count = 0;
//         while (num != 0) {
//             count += num & 1;
//             num = num >> 1;
//         }
//         return count;
//     }

//     static int complement(int num) {
//         int maskLength = Integer.toBinaryString(num).length();
//         int mask = (1 << maskLength) - 1;
//         int complement = num ^ mask;
//         return  complement;
//     }

//     public static void main(String[] args) {
//         System.out.println("Int to Binary of 10 : " + intTOBinary(10));
//         System.out.println("Binary to Int of 1011 : " + binaryToInt("1011"));
//         System.out.println("Count bits in 10 : " + countBits(10));
//         System.out.println("complement of 10 : " + complement(10));
//     }
// }


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
