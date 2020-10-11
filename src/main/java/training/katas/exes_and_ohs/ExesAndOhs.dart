bool XO(str) {
  // your code here
  var lowerCased = str.toLowerCase();
  return lowerCased.runes.where((int i) {
    return i == 'x'.codeUnitAt(0);
  }).length == lowerCased.runes.where((int i) {
    return i == 'o'.codeUnitAt(0);
  }).length;
}

void main() {
  print(XO("xox"));
}
