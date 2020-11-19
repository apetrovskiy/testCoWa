package training.katas.number_of_people_in_the_bus;

import java.util.ArrayList;

import org.junit.Test;

import static org.junit.Assert.assertEquals;
import org.junit.runners.JUnit4;
import training.katas.number_of_people_in_the_bus.Metro;

public class NumberOfPeopleInTheBusTest {
    Metro metro = new Metro();

    @Test
    public void test1() {
        ArrayList<int[]> list = new ArrayList<int[]>();
        list.add(new int[] { 10, 0 });
        list.add(new int[] { 3, 5 });
        list.add(new int[] { 2, 5 });
        assertEquals(5, metro.countPassengers(list));
    }

}