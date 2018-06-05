public class MyStack {
    public static void main(String[] args) {
        MyStackArray<String> stack = new MyStackArray<String>();
        stack.push("Rajesh");
        stack.push("Murthy");
        stack.push("Lalitha");
        System.out.println(stack.pop());

        MyStackList<String> stackList = new MyStackList<String>();
        stackList.push("Rajesh");
        stackList.push("Murthy");
        stackList.push("Lalitha");
        System.out.println(stackList.pop());
    }
}
