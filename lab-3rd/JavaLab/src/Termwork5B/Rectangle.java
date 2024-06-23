package Termwork5B;

public class Rectangle {
    int length, width;
    Rectangle(int length, int width){
        this.length = length;
        this.width = width;
    }

    int computerArea(){
        return length * width;
    }

    int computePerimeter(){
        return 2*(length + width);
    }
    
}