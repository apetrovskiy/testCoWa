package training.katas.NumberOfPeopleInTheBus

fun people(busStops: Array<Pair<Int, Int>>): Int {
    // code here
    return busStops.map { (a, _) -> a }.sum() - busStops.map { (_, b) -> b }.sum()
}
