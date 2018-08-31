import java.lang.reflect.Array;
import java.util.*;

public class sym {
    Hashtable<Integer, Integer> hashtable;
    int[] example = {1, 2, 3};
    int[][] arraysofInt;
    public ArrayList<Integer> sym1(int[][] args) {
        for(int i = 0; i < args.length; i++) {
            int[] array1 = args[i];
            for(int j = 0; j < array1.length; j++) {
                if(hashtable.containsKey(array1[j])) {
                    hashtable.remove(array1[j])
                }
                else {
                    hashtable.put(array1[j],1);
                }
            }
        }
        Enumeration<Integer> enm = hashtable.keys();
        ArrayList<Integer> list1  = Collections.list(enm);
        return list1;
    }

    public void main(String[] args) {
        StringBuilder sb = new StringBuilder();
        int[][] temp = {{1, 2, 3},
        {5, 2, 1, 4}};
        ArrayList<Integer> alist = sym1(temp);
        System.out.println(();

    }
}
