package Termwork5B;

public class Cuboid extends Rectangle {
    int height;
    Cuboid(int length, int width, int height){
        super(length, width);
        this.height = height;
    }

    int computerArea(){
        return 2*(length + width + height);
    }

    int computePerimeter(){
      return    4*(length + width + height);
    }

    int computeVolume(){
       return super.computerArea() * height;
    }
}