import java.util.ArrayList;
import java.util.List;

public class P03MaxCandy {
    public static void main(String[] args) {
        int[] candy = {2,3,5,1,3};
        Solution s = new Solution();
        List<Boolean> hasMaxCandy = s.kindsWithMaxCandy(candy, 3);
        for (Boolean status : hasMaxCandy) {
            System.out.println(status);
        }
        
    }
}


class Solution{

    public ArrayList<Boolean> kindsWithMaxCandy(int[] candies, int extraCandy){

        ArrayList<Boolean> hasMaxCandy = new ArrayList<Boolean>();
        int maxCandy = -1;
        for(int candy : candies){
            if(candy>maxCandy) maxCandy = candy; 
        }

        for(int candy : candies){
            if(candy + 10 >= maxCandy) {
                hasMaxCandy.add(true);
                continue;
            }
            hasMaxCandy.add(false);
        }

        return hasMaxCandy;
    }
}