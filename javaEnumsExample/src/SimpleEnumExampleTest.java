import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class SimpleEnumExampleTest {
    @Test
    public void simpleEnumExampleOutsideClassTest(){
        Days day = Days.SUNDAY;
        System.out.println("Days enum is set a value: "+day);
        assertEquals(Days.valueOf("SUNDAY"), day);
    }

}
