package TermWork9;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        String s1, s2;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the String #1 :");
        s1 = sc.next().toLowerCase();
        System.out.println("\nEnter the String #2 :");
        s2 = sc.next().toLowerCase();
        check_anagrams(s1, s2);
        sc.close();
    }

    static void check_anagrams(String s1, String s2) {
        char c1[] = s1.toCharArray();
        char c2[] = s2.toCharArray();
        Arrays.sort(c1);
        Arrays.sort(c2);
       String s3 = new String(c1);
       String s4 = new String(c2);
        System.out.println(s1 + " and " + s2 + " are anagrams : " + s3.equalsIgnoreCase(s4));
    }

}

// static String sort(char arr[]) {
//     for (int i = 0; i < arr.length; i++) {
//         for (int j = 0; j < arr.length - 1; j++) {
//             if (arr[j] > arr[j + 1]) {
//                 char temp = arr[j];
//                 arr[j] = arr[j + 1];
//                 arr[j + 1] = temp;
//             }
//         }
//     }
//     return new String(arr);
// }