function rowSumOddNumbers(n) {
    "use strict";
    var result = 0;
    var maxNum = n * (n + 1) - 1;
    for (i = maxNum; i > maxNum - 2 * n; i - 2) {
        result += i;
    }
    return result;
}
module.exports = { rowSumOddNumbers };