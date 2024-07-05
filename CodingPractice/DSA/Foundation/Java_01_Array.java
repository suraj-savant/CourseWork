
import java.util.Random;

public class Java_01_Array {
    public static void main(String[] args) {

        MyArray arr = new MyArray();
        for (int i = 0; i < 10; i++) {
            arr.append(new Random().nextInt(100));
        }

        arr.printArray();
        arr.reverse();
        arr.printArray();
    }
}

class MyArray {
    int[] arr = new int[100];
    int length = 0;

    MyArray() {

    }

    void printArray() {
        for (int i = 0; i < length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    void append(int elemt) {
        arr[length++] = elemt;
    }

    void removeAt(int index) {
        for (int i = index; i < length; i++) {
            arr[i] = arr[i + 1];
        }
        length--;
    }

    void insertAt(int index, int elemt) {
        for (int i = length - 1; i > index; i--) {
            arr[i + 1] = arr[i];
        }
        arr[index] = elemt;
        length++;
    }

    void reverse() {
        int i = 0;
        int j = length - 1;
        int temp;
        while (i < j) {
            temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            i++;
            j--;
        }
    }
}
