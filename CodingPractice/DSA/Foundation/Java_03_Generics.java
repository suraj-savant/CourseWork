package Foundation;

import org.w3c.dom.ls.LSOutput;

public  class Java_03_Generics {
    public static void main(String[] args) {
        MyArray<String> arr = new MyArray<>(3);
        arr.add("Hii");
        arr.add("Hello");

        for (int i = 0; i < arr.size(); i++) {
            System.out.println(arr.getItem(i));
        }
    }

}

class MyArray<T>{
    final private T[] arr;
    private  int index;

    MyArray(int size){
        arr = (T[]) new Object[size];
        index = 0;
    }

    void add(T item){
        arr[index++] = item;
    }

    T getItem(int index){
        return  arr[index];
    }

    int size(){
        return  index + 1;
    }
}


//
//public class Java_03_Generics {
//    public static void main(String[] args) {
//        MyGenericClass<String> obj = new MyGenericClass<>();
//        obj.setValue("Hello World");
//        System.out.println(obj.getValue());
//    }
//}
//
//class MyGenericClass<T>{
//    private T value;
//    MyGenericClass(){}
//    MyGenericClass(T value){
//        this.value = value;
//    }
//
//    public void setValue(T value){
//        this.value = value;
//    }
//
//    public T getValue(){
//        return this.value;
//    }
//}