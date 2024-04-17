package main.com;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

class DollarTest {
    @Test
    public void testMultiplication() {
        Money five = Money.dollar(5);
        assertEquals(Money.dollar(10), five.times(2));
        assertEquals(Money.dollar(15), five.times(3));
    }
}