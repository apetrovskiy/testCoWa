library training.katas.ConvertBooleanValuesToStringsYesOrNo;

import "package:test/test.dart";
// import "package:solution/solution.dart";
import '../../../../../main/java/training/katas/ConvertBooleanValuesToStringsYesOrNo/ConvertBooleanValuesToStringsYesOrNo.dart';

void main() {
  group('Convert boolen value basic tests', () {
    test('Yes/No', () {
      expect(bool_to_word(true), equals("Yes"));
      expect(bool_to_word(false), equals("No"));
    });
  });
}