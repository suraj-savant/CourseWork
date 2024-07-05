
import java.util.*;

public class Java_00 {

    public static void main(String[] args) {
       List<Integer> lst = new ArrayList<Integer>();
        for (int i = 0; i <5 ; i++) {
            lst.add(new Random().nextInt(10)) ;
        }
        lst.add(4);
        lst.add(12);
        lst.add(15);
        System.out.println(lst);

        System.out.println("Remove last using index");
        lst.remove(lst.size() - 1);
        System.out.println(lst);

        System.out.println("Remove first 4 using value");
        lst.remove(Integer.valueOf(4));
        System.out.println(lst);

        System.out.println("Update first element to 100");
        lst.set(0, 100);
        System.out.println(lst);

    }
}


// Set and Tree set
//public class Java_00 {
//    public static void main(String[] args) {
//        List<String> list = new ArrayList<>(
//                Arrays.asList(new String[]{"Suraj", "Aman", "Rohit", "Rajesh"})
//        );
//
//        // Elements are added depends on hash code computed order may be different
//        HashSet<String> hashSet = new HashSet<>(list);
//        hashSet.add("Suraj");
//        hashSet.add("Aman");
//
//        // Elements are ordered in particular order based on comparator
//        TreeSet<String> treeSet = new TreeSet<>(list);
//        treeSet.add("Suraj");
//        treeSet.add("Aman");
//
//        System.out.println("Hash Set : " + hashSet);
//        System.out.println("Tree Set : " + treeSet);
//    }
//}


// Hash Map Example
//public class Java_00 {
//
//    public static void main(String[] args) {
//        String str = "aaabb baaaccc";
//        HashMap<Character, Integer> characterCounts = new HashMap<>();
//        for (char c : str.toCharArray()) {
//            if(c == ' ') continue;
//            if (characterCounts.containsKey(c)) {
//                characterCounts.put(c, characterCounts.get(c) + 1);
//                continue;
//            }
//            characterCounts.put(c, 1);
//        }
//
//        for(char key:characterCounts.keySet()){
//            System.out.println(key + " " + characterCounts.get(key));
//        }
//
//    }
//}

 // Input Output

//public class Java_00 {
//    public static void main(String[] args) {
//        Scanner sc = new Scanner(System.in);
//
//        String name = sc.nextLine();
//        int age = sc.nextInt();
//        char gender = sc.next().charAt(0);
//        boolean isMarried = sc.nextBoolean();
//
//        System.out.println("Hello " + name + " you are " + age + " years old.");
//        System.out.println("Your gender is " + (gender == 'M' ? "Male" : "Female"));
//        System.out.println("You are " + (isMarried?"":"not")   + " married");
//    }
//}
