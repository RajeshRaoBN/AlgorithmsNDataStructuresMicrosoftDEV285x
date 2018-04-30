import java.util.Arrays;

public class BubbleSort {
    public static void main(String[] args) {
        int[] array = {4,9,7,1,3,6,5};
        bubbleSortMy(array);
    }
    static void bubbleSort(int[] lst) {
        int n = lst.length;
        boolean swapped;
        do
        {
            swapped = false;
            for (int i = 0; i < n-1; i++) {
                if (lst[i] > lst[i+1]) {
                    int temp = lst[i];
                    lst[i] = lst[i+1];
                    lst[i+1] = temp;
                    swapped = true;
                }
            }
        } while (swapped == true);

        System.out.println(Arrays.toString(lst));
    }
    static void bubbleSortMy(int[] iArray){
        for(int j = iArray.length - 1; j > 0; j--) {
            for (int i = 0; i < j; i++) {
                if(iArray[i] > iArray[i + 1]) {
                    int sw = iArray[i];
                    iArray[i] = iArray[i + 1];
                    iArray[i + 1] = sw;
                }
            }
        }
        System.out.println(Arrays.toString(iArray));
    }
}
