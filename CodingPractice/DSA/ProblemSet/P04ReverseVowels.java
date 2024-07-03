
class Solution{
    Boolean isVowel(char c){
        char[] vowels = {'a', 'e', 'i', 'o', 'u'};
        for (char vowel : vowels) {
            if(vowel == c)
                return true; 
            }  
        return false;
    }
    String reverseVowel(String s){
        char[] charArray = s.toCharArray();
        
        int i = -1, j= s.length() ;
        char temp;
        while (true) {
            while( !isVowel(charArray[++i]));            
            while( !isVowel(charArray[--j]));
            if(i>j) break;
            temp = charArray[i];
            charArray[i] = charArray[j];
            charArray[j] = temp;
            
        }

        for (char c : charArray) {
            System.out.println(c);
        }
        return  new String(charArray);

    }
}


public class P04ReverseVowels {
    public static void main(String[] args) {
        Solution s = new Solution();
        String revrse = s.reverseVowel("aobbei");
        System.out.println(revrse);
    }
}
