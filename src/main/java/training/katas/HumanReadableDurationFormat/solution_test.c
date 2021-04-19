/*
#include <criterion/criterion.h>

char *formatDuration (int n);

void shouldBe (int n, const char *expected) {
  char *result = formatDuration (n);
  cr_assert_str_eq (result, expected, "Got '%s', expected '%s'", result, expected);
  free (result);
}

Test (formatduration, sample) {
  shouldBe (0, "now");
  shouldBe (1, "1 second");
  shouldBe (3600, "1 hour");
  shouldBe (120, "2 minutes");
  shouldBe (62, "1 minute and 2 seconds");
  shouldBe (3662, "1 hour, 1 minute and 2 seconds");
}
*/