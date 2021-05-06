function rowSumOddNumbers(n) {
    let result = 0;
    const maxNum = n * (n + 1) - 1;
    for (let i = maxNum; i > maxNum - 2 * n; i -= 2) {
        result += i;
    }
    return result;
}
module.exports = { rowSumOddNumbers };