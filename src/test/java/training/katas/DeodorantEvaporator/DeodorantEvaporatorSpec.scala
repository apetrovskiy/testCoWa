package training.katas.DeodorantEvaporator

// You can test using ScalaTest (http://www.scalatest.org/).
import org.scalatest.{FlatSpec, Matchers}

// TODO: replace this example test with your own, this is just here to demonstrate usage.
// See http://www.scalatest.org/at_a_glance for example usages
class DeodorantEvaporatorSpec extends FlatSpec with Matchers {
  "evaporator(10,10,10)" should "return 22" in {
    Sol.evaporator(10, 10, 10) should be(22)
  }
  "evaporator(10,10,10)" should "return 22" in {
    Sol.evaporator(10, 10, 5) should be(29)
  }
  "evaporator(10,10,10)" should "return 22" in {
    Sol.evaporator(100, 5, 10) should be(59)
  }
}
