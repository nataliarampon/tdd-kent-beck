package main.com;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

class FrancTest {
    @Test
    public void testMultiplication() {
        Franc five = new Franc(5);
        assertEquals(new Franc(10), five.times(2));
        assertEquals(new Franc(15), five.times(3));
    }
}