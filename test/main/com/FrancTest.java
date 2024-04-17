package main.com;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

class FrancTest {
    @Test
    public void testMultiplication() {
        Money five = Money.franc(5);
        assertEquals(Money.franc(10), five.times(2));
        assertEquals(Money.franc(15), five.times(3));
    }
}