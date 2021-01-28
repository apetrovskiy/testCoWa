package training.katas.HumanReadableDurationFormat

import org.junit.Test

class TestExample {
  @Test
  void "Basic Tests"() {
    assert Kata.formatDuration(1) == "1 second"
    assert Kata.formatDuration(62) == "1 minute and 2 seconds"
    assert Kata.formatDuration(120) == "2 minutes"
    assert Kata.formatDuration(3600) == "1 hour"
    assert Kata.formatDuration(3662) == "1 hour, 1 minute and 2 seconds"
  }
}
