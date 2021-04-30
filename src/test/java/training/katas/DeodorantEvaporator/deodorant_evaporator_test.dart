library training.katas.DeodorantEvaporator;

// See https://pub.dartlang.org/packages/test
import "package:test/test.dart";
// import "package:solution/solution.dart";
import '../../../../../main/java/training/katas/DeodorantEvaporator/deodorant_evaporator_test.dart';

void main() {
  test("Sample Deodorant Evaporator Test Cases", () {
    expect(evaporator(10, 10, 10), equals(22));
    expect(evaporator(10, 10, 5), equals(29));
    expect(evaporator(100, 5, 5), equals(59));
  });
}
