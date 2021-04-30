function evaporator(content, evap_per_day, threshold) {
    var nthDay = 0;
    var absoluteThreshold = (content * threshold) / 100;
    while (content > absoluteThreshold) {
        nthDay += 1;
        content *= (100 - evap_per_day) / 100;
    }
    return nthDay;
}
module.exports = { evaporator };