library training.katas.SumOfOddNumbers;

import "package:test/test.dart";
// import "package:solution/solution.dart";
import '../../../../../main/java/training/katas/SumOfOddNumbers/sum_of_odd_numbers.dart';

void main() {
  group('Sum of odd numbers basic tests', () {
    test('Sum', () {
      expect(rowSumOddNumbers(1), equals(1));
      expect(rowSumOddNumbers(2), equals(8));
      expect(rowSumOddNumbers(13), equals(2197));
      expect(rowSumOddNumbers(19), equals(6859));
      expect(rowSumOddNumbers(41), equals(68921));
        expect(rowSumOddNumbers(42), equals(74088));
  expect(rowSumOddNumbers(74), equals(405224));
expect(rowSumOddNumbers(86), equals(636056));
expect(rowSumOddNumbers(93), equals(804357));
expect(rowSumOddNumbers(101), equals(1030301));
    });
  });
}

/*
import "package:test/test.dart";
import "package:solution/solution.dart";

void main() {
  group("basic tests", () {
    test("Testing for 1", () => expect(rowSumOddNumbers(1), equals(1)));
    test("Testing for 2", () => expect(rowSumOddNumbers(2), equals(8)));
    test("Testing for 13", () => expect(rowSumOddNumbers(13), equals(2197)));
    test("Testing for 19", () => expect(rowSumOddNumbers(19), equals(6859)));
    test("Testing for 41", () => expect(rowSumOddNumbers(41), equals(68921)));
    test("Testing for 42", () => expect(rowSumOddNumbers(42), equals(74088)));
    test("Testing for 74", () => expect(rowSumOddNumbers(74), equals(405224)));
    test("Testing for 86", () => expect(rowSumOddNumbers(86), equals(636056)));
    test("Testing for 93", () => expect(rowSumOddNumbers(93), equals(804357)));
    test("Testing for 101", () => expect(rowSumOddNumbers(101), equals(1030301)));
  });
}
*/
