class Prime{
    public static void main(String args[]){
        int num = 17;
        int counter = 2;
        while(counter < num/2){
            if(num % counter == 0){
                System.out.println("Not prime");
                return;
            }
            counter++;
        }

        System.out.println("Prime Number");
    }
}