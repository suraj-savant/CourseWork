
class Solution {
    public String reverseWords(String s) {
        String[] splitString = s.split(" ");
        int i=0;
        
        int j = splitString.length - 1;
        while(i < j){
            String temp = splitString[i];
            splitString[i] = splitString[j];
            splitString[j] = temp;
            i++; j--;
            
        }
        String output = "";
        for (String string : splitString) {
            output += " "+string;
        }
        return output.trim();
    }
}

public class P05ReverseWords {
    public static void main(String[] args) {
        Solution s = new Solution();
        String ip = "hii i am suraj";
        System.out.println(s.reverseWords(ip));
    }
}

