function pyramid(n) {
    let result = [];
    if (n == 0) {
        return result;
    }
    for (let i = 1; i <= n; i++) {
        result.push(Array.from({ length: i }, (v, j) => 1));
    }
    return result;
}
module.exports = { pyramid };