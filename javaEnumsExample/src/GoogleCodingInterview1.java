import java.util.Hashtable;

public class GoogleCodingInterview1 {
    public static char Analyse(String word) {
        char firstChar = ' ';
        Hashtable<Character, Integer> hashtable = new Hashtable<Character, Integer>();
        for(char ch: word.toCharArray()) {
            Character C = Character.valueOf(ch);
            if(hashtable.containsKey(C))
                return ch;
            hashtable.put(C, 1);
        }
        return firstChar;
    }
    public static void main(String args[]) {
        System.out.println(Analyse("BCABA"));
    }
}
