
public class Java_06_LinkedList {
    public static void main(String[] args) {
        LinkedList ll = new LinkedList();
        ll.addFirst(10);
        ll.addFirst(20);
        ll.addFirst(30);
        ll.addLast(100);
        ll.printList();
        ll.reverseList();
        ll.printList();
    }
}



class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
    }
}

class LinkedList {
    Node head;

    void addFirst(int data) {
        if (head == null) {
            head = new Node(data);
            return;
        }
        Node newNode = new Node(data);
        newNode.next = head;
        head = newNode;
    }

    void addLast(int data){
        if(head == null){
            head = new Node(data);
            return;
        }
        Node temp = head;
        while (temp.next != null) {
            temp = temp.next;
        }
        temp.next = new Node(data);
    }

    void reverseList(){
     Node reverse = null;
     Node temp = head;
     while (temp != null) {
        Node cur = temp;
        temp = temp.next;
        if(reverse == null){
            reverse = cur;
            reverse.next = null;
            continue;
        }
        cur.next = reverse;
        reverse = cur;
     }

     head = reverse;
    }
    
    void printList() {
        if (head == null) {
            System.out.println("List is empty");
            return;
        }
        Node temp = head;
        while (temp != null) {
            System.out.print(temp.data + " -> ");
            temp = temp.next;
        }
        System.out.println();

    }
}
