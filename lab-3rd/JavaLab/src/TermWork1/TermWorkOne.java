package TermWork1;

import java.util.Scanner;

public class TermWorkOne {
   static int studentCount = 5;
   static int subjectCount = 3;
    static int[][] marks = new int[studentCount][subjectCount];
    static int[] totalMarks = new int[studentCount];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < studentCount; i++) {
            System.out.println("Enter the marks of student : " + (i + 1));
            int total = 0;
            for (int j = 0; j < subjectCount; j++) {
                marks[i][j] = sc.nextInt();
                total += marks[i][j];
            }
            totalMarks[i] = total;
        }
        sc.close();
        for (int i = 0; i < studentCount; i++) {
            System.out.println("Report of student " + (i + 1));
            for (int j = 0; j < subjectCount; j++) {
                System.out.println(marks[i][j]);
            }
            System.out.println("Total marks " + totalMarks[i]);
            System.out.println("Average marks " + averageMarks(marks[i]) + "\n");
        }
    }

    public static double averageMarks(int[] marks) {
        int min = 1000;
        int sum = 0;
        for (int mark : marks) {
            sum += mark;
            if (mark < min) {
                min = mark;
            }
        }
        
        return Math.ceil((sum - min) / 2);
    }
}
