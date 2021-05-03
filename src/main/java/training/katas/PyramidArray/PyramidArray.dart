List<List<int>> pyramid(int n) {
  if (n == 0) {
    return new List();
  }
  var result = new List.filled(n, [], growable: false);
  for (var i = 1; i <= n; i++) {
    result[i - 1] = List<int>.filled(i, 1, growable: false).cast<int>();
  }
  return result.cast<List<int>>();
}
