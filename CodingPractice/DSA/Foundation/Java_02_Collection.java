import java.util.*;
import java.util.Map.Entry;

public class Java_02_Collection {

    public static void main(String[] args) {
        Map<Character, Integer> map = new HashMap<>();
        String ip = "aabaacaac bbaaa";
        char[] arr = ip.toCharArray();
        for (char c : arr) {
            if (c == ' ')
                continue;
            if (map.keySet().contains(c)) {
                map.put(c, map.get(c) + 1);
                continue;
            }
            map.put(c, 1);
        }

        for( Entry<Character, Integer> entry : map.entrySet()){
            System.out.println(entry.getKey() + " " + entry.getValue());

        }

    }
}

// package Foundation;
// import java.util.*;

// public class Java_02_Collection {
// public static void main(String[] args) {
// // list to array
// ArrayList<Integer> lst = new ArrayList<>();
// lst.add(2);
// lst.add(3);
// lst.add(2);
// lst.add(1);
// Integer[] arr = lst.toArray(new Integer[0]);
// for (int i: arr) System.out.print(i + ",");

// // Array to list
// Integer[] numbers = new Integer[] { 1, 2, 3 };
// List<Integer> list = Arrays.asList(numbers);
// System.out.println(list);
// }
// }

// // Methods common to all Collection
// class CollectionExample {
// public static void main(String[] args) {
// // Creating an ArrayList and adding elements
// List<String> list = new ArrayList<>();
// list.add("apple");
// list.add("banana");
// list.add("cherry");

// // Using common methods for all collections
// System.out.println("List: " + list);
// System.out.println("Size of list: " + list.size());
// System.out.println("Is list empty : " + list.isEmpty());

// // Adding more elements using addAll method
// List<String> moreFruits = Arrays.asList("date", "elderberry");
// list.addAll(moreFruits);
// System.out.println("List after adding more elements: " + list);

// // Removing an element
// list.remove("banana");
// System.out.println("List after removing 'banana': " + list);

// // Checking if an element exists
// boolean containsCherry = list.contains("cherry");
// System.out.println("Does list contain 'cherry'? " + containsCherry);

// // Iterating over elements using an iterator
// Iterator<String> iterator = list.iterator();
// System.out.print("Iterating over list: ");
// while (iterator.hasNext()) {
// System.out.print(iterator.next() + " ");
// }
// System.out.println();
// }
// }

// //List example
// class ListExample {
// public static void main(String[] args) {
// // Creating an ArrayList and adding elements
// List<String> list = new ArrayList<>();
// list.add("apple");
// list.add("banana");
// list.add("cherry");

// // Adding an element at a specific index
// list.add(1, "orange");
// System.out.println("List after adding 'orange' at index 1: " + list);

// // Removing an element at a specific index
// String removedElement = list.remove(2);
// System.out.println("List after removing element at index 2 ('cherry'): " +
// list);

// // Getting an element at a specific index
// String elementAtIndex = list.get(0);
// System.out.println("Element at index 0: " + elementAtIndex);

// // Replacing an element at a specific index
// list.set(2, "grape");
// System.out.println("List after replacing element at index 2 with 'grape': " +
// list);

// // Sorting elements
// Collections.sort(list);
// System.out.println("List after sorting: " + list);
// }
// }

// // Set example
// class SetExample {
// public static void main(String[] args) {
// // Creating a HashSet and adding elements
// Set<String> set = new HashSet<>();
// set.add("apple");
// set.add("banana");
// set.add("cherry");

// // Adding duplicate elements (ignored in Set)
// set.add("apple");
// System.out.println("Set: " + set);

// // Removing an element
// set.remove("banana");
// System.out.println("Set after removing 'banana': " + set);

// // Checking if an element exists
// boolean containsCherry = set.contains("cherry");
// System.out.println("Does set contain 'cherry'? " + containsCherry);

// // Iterating over elements using an iterator
// Iterator<String> iterator = set.iterator();
// System.out.print("Iterating over set: ");
// while (iterator.hasNext()) {
// System.out.print(iterator.next() + " ");
// }
// System.out.println();
// }
// }

// // Hash Map example
// class MapExample {
// public static void main(String[] args) {
// // Creating a HashMap and adding key-value pairs
// Map<String, Integer> map = new HashMap<>();
// map.put("apple", 10);
// map.put("banana", 20);
// map.put("cherry", 30);

// // Adding a new key-value pair
// map.put("date", 40);
// System.out.println("Map after adding ('date', 40): " + map);

// // Removing a key-value pair
// map.remove("banana");
// System.out.println("Map after removing ('banana', 20): " + map);

// // Getting the value for a specific key
// Integer value = map.get("apple");
// System.out.println("Value for 'apple': " + value);

// // Checking if a key exists
// boolean containsKey = map.containsKey("cherry");
// System.out.println("Does map contain key 'cherry'? " + containsKey);

// // Iterating over keys using keySet()
// System.out.print("Iterating over map keys: ");
// for (String key : map.keySet()) {
// System.out.print(key + " ");
// }
// System.out.println();
// }
// }

// //Linked list example
// class QueueExample {
// public static void main(String[] args) {
// // Creating a LinkedList as a Queue and adding elements
// Queue<String> queue = new LinkedList<>();
// queue.add("apple");
// queue.add("banana");
// queue.add("cherry");

// // Removing and retrieving the head of the queue
// String head = queue.poll();
// System.out.println("Removed from queue (head): " + head);
// System.out.println("Queue after removing head: " + queue);

// // Adding elements to the queue
// queue.offer("date");
// queue.offer("elderberry");
// System.out.println("Queue after adding 'date' and 'elderberry': " + queue);

// // Peeking at the head of the queue (without removing)
// String peeked = queue.peek();
// System.out.println("Peeked at head of queue: " + peeked);
// }
// }

// import java.util.*;

// class Java_02_Collection {
// public static void main(String[] args) {
// char[] chars = { 'a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b',
// 'b', 'b', 'b', 'b', 'b' };
// HashMap<Character, Integer> charMap = new HashMap<Character, Integer>();
// for (char c : chars) {
// if (!charMap.containsKey(c)) {
// charMap.put(c, 0);
// }
// charMap.put(c, charMap.get(c) + 1);
// }

// int compressionCount = 0;

// for (int i : charMap.values()) {

// String str = String.valueOf(i);
// if (str.length() == 1) {
// compressionCount += 1;
// continue;
// }
// compressionCount += str.length() + 1;
// }

// int i = -1;
// for (Map.Entry<Character, Integer> entry : charMap.entrySet()) {
// if (entry.getValue() == 1) {
// chars[++i] = entry.getKey();

// continue;
// }
// chars[++i] = entry.getKey();

// String str = String.valueOf(entry.getValue());
// System.out.println(str);

// for (int j = 0; j < str.length(); j++) {
// chars[++i] = str.charAt(j);

// }

// }

// for (int j = 0; j < compressionCount; j++) {
// System.out.print(chars[j]);

// }

// }
// }
