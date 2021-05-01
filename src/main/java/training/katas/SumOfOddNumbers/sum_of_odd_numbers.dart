library training.katas.SumOfOddNumbers

int rowSumOddNumbers(int n) {
  var maxNum = n * (n + 1) - 1;
  var result = 0;
  for (var i = maxNum; i > maxNum - n * 2; i -= 2){
    result += i;
  }
  return result;
}