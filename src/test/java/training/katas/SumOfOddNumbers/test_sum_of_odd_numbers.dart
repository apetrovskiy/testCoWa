library training.katas.SumOfOddNumbers

import "package:test/test.dart";
// import "package:solution/solution.dart";
import '../../../../../main/java/training/katas/SumOfOddNumbers/sum_of_odd_numbers.dart;

void main() {
  group('Sum of odd numbers basic tests', () {
    test('Sum', () {
      expect(rowSumOddNumbers(1), equals(1));
      expect(rowSumOddNumbers(2), equals(8));
      expect(rowSumOddNumbers(13), equals(2197));
      expect(rowSumOddNumbers(19), equals(6859));
      expect(rowSumOddNumbers(41), equals(68921));
    });
  });
}
