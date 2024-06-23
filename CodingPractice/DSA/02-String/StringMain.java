
public class StringMain {
    public static void main(String[] args) {
        String s1 = "abc", s2="pqrstuv";
        int i=0;
        int j=0;
       String op = "";
        while (i<s1.length() && j<s2.length()) {
            op += s1.substring(i, ++i)+s2.substring(j, ++j);
            
        }
        if(i<s1.length()){
            op += s1.substring(i, s1.length());
        }
        if(j<s2.length()){
            op += s2.substring(i, s2.length());
        }
        System.out.println(op);
    }
}
