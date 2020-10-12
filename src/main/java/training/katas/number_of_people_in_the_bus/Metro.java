package training.katas.number_of_people_in_the_bus;

import java.util.ArrayList;

class Metro {

  public static int countPassengers(ArrayList<int[]> stops) {
    // Code here!
    return stops.stream().mapToInt(item -> item[0]).sum() - stops.stream().mapToInt(item -> item[1]).sum();
  }
}
