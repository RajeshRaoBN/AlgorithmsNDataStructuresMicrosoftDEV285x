import java.util.Arrays;

public class SelectionSort {
    public static void main(String[] args) {
        int[] ix = {4,9,7,1,3,6,5};
        //System.out.println(Arrays.toString(ix));
        //selectionSort(ix);
        selectionSortMy(ix);
    }
    static void selectionSort(int[] lst) {
        // get the length
        int n = lst.length;
        for (int i = 0; i < n; i++) {
            int index = 0;
            int smallest = lst[i];
            for (int j = i; j < n; j++) {
                if (lst[j] < smallest) {
                    smallest = lst[j];
                    index = j;
                }
                int temp = lst[i];
                lst[i] = smallest;
                lst[index] = temp;
            }
        }
        System.out.println(Arrays.toString(lst));
    }
    static void selectionSortMy(int[] lst1) {
        //System.out.println(Arrays.toString(lst1));
        for(int i = 0; i < lst1.length; i++){
            int smallestNumber = lst1[i];
            int sNIndex = i;
            for(int j = i + 1; j < lst1.length; j++) {
                if(lst1[j] < smallestNumber) {
                    smallestNumber = lst1[j];
                    sNIndex = j;
                }
            }
            int swap = lst1[i];
            lst1[i] = lst1[sNIndex];
            lst1[sNIndex] = swap;
        }
        System.out.println(Arrays.toString(lst1));
    }
}
