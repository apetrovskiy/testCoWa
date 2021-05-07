
package training.katas.number_of_people_in_the_bus

fun people(busStops: Array<Pair<Int, Int>>): Int {
    // code here
    return busStops.map { (a, _) -> a }.sum() - busStops.map { (_, b) -> b }.sum()
}
