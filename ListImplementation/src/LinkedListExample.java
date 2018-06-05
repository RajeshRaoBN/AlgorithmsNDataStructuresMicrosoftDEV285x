import java.util.LinkedList;

public class LinkedListExample {
    public String bookName;
    public int millionsSold;

    public LinkedListExample next;

    public LinkedListExample(String bookName, int millionsSold) {
        this.bookName = bookName;
        this.millionsSold = millionsSold;
    }

    public void display() {
        System.out.println(bookName + ": " + millionsSold + ",000,000");
    }

    public String toString() {
        return bookName;
    }

    public static void main(String[] args) {

    }
}

class Linklist{
    public LinkedListExample firstLink;

    public Linklist() {
        firstLink = null;
    }
}