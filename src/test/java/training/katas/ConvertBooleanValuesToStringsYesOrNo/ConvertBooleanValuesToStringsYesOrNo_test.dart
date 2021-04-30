import "package:test/test.dart";
// import "package:solution/solution.dart";
import "../../../../../main/java/training/katas/ConvertBooleanValuesToStringsYesOrNo/ConvertBooleanValuesToStringsYesOrNo.dart";

void main() {
  test('Tests', () {
    expect(bool_to_word(true), equals("Yes"));
    expect(bool_to_word(false), equals("No"));
  });
}