package Foundation;

class Java_04_String{

        public static void main(String[] args) {
            // Example string
            String str = "hello world";

            // 1. charAt
            char charAtExample = str.charAt(1);
            System.out.println("Character at index 1: " + charAtExample);

            // 2. length
            int lengthExample = str.length();
            System.out.println("Length of string: " + lengthExample);

            // 3. substring (beginIndex, endIndex)
            String substringExample = str.substring(0, 5);
            System.out.println("Substring from index 0 to 5: " + substringExample);

            // 4. substring (beginIndex to end)
            String substringToEndExample = str.substring(6);
            System.out.println("Substring from index 6 to end: " + substringToEndExample);

            // 5. contains
            boolean containsExample = str.contains("world");
            System.out.println("String contains 'world': " + containsExample);

            // 6. indexOf
            int indexOfExample = str.indexOf('o');
            System.out.println("First occurrence of 'o': " + indexOfExample);

            // 7. toUpperCase
            String upperCaseExample = str.toUpperCase();
            System.out.println("Uppercase string: " + upperCaseExample);

            // 8. toLowerCase
            String lowerCaseExample = str.toLowerCase();
            System.out.println("Lowercase string: " + lowerCaseExample);

            // 9. replace
            String replaceExample = str.replace('l', 'p');
            System.out.println("String with 'l' replaced by 'p': " + replaceExample);

            // 10. split
            String[] splitExample = str.split(" ");
            System.out.println("String split by space: ");
            for (String part : splitExample) {
                System.out.println(part);
            }
        }


}

//
//public class Java_04_String {
//    public static void main(String[] args) {
//        String s1 = "abc", s2="pqrstuv";
//        int i=0;
//        int j=0;
//        String op = "";
//        while (i<s1.length() && j<s2.length()) {
//            op += s1.substring(i, ++i)+s2.substring(j, ++j);
//        }
//        if(i<s1.length()){
//            op += s1.substring(i);
//        }
//        if(j<s2.length()){
//            op += s2.substring(i);
//        }
//        System.out.println(op);
//    }
//}
