public class LinearSearch {
    public static void main(String[] args) {
        int[] ix = {4,9,7,1,3,6,5};
        linearSearch(ix, 5);
    }
    static void linearSearch(int[] lst, int v) {
        int n = lst.length;
        for (int i = 0; i < n; i++) {
            if (lst[i] == v) {
                System.out.println("found! It is at" + i);
                return;
            }
        }
        System.out.println("the element is not in the array");
        return;
    }
}
