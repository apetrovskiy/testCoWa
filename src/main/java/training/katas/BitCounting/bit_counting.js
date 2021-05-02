var countBits = function(n) {
    let counter = 0;
    const maxExtent = Math.pow(2, 20);
    for (let i = maxExtent; i > 0; i /= 2) {
        if (n > i) {
            n -= i;
            counter++;
        }
    }
    return counter;
};
module.exports = { countBits };