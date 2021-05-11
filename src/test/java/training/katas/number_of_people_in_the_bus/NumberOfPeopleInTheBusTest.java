package training.katas.number_of_people_in_the_bus;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.ArrayList;
import org.junit.jupiter.api.Test;

public class NumberOfPeopleInTheBusTest {
  @SuppressWarnings("PMD")
  Metro metro = new Metro();

  @SuppressWarnings("PMD")
  @Test
  public void test1() {
    var list = new ArrayList<int[]>();
    list.add(new int[] {10, 0});
    list.add(new int[] {3, 5});
    list.add(new int[] {2, 5});
    assertEquals(5, metro.countPassengers(list));
  }
}
