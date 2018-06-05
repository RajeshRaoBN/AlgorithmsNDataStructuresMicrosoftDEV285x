import java.util.LinkedList;

public class LinkedListExample2 {
    public static void main(String[] args) {
        LinkedList<String> ll = new LinkedList<String>();
        ll.add("Rajesh");
        ll.add("Sultan");
        ll.add("Khan");
        ll.add("Khanan");
        System.out.println(ll.size());
        System.out.println(ll.get(2));
        ll.add(2, "Bijnoor");
        System.out.println(ll.size());
        System.out.println(ll.get(2));
        System.out.println(ll.get(3));
    }
}
