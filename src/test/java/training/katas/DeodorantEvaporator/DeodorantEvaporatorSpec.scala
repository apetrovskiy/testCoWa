package training.katas.DeodorantEvaporator

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments.of
import org.junit.jupiter.params.provider.{Arguments, MethodSource}
import org.scalatest.flatspec.AnyFlatSpec
import org.scalatest.matchers.should.Matchers

// You can test using ScalaTest (http://www.scalatest.org/).
//import org.scalatest.{FlatSpec, Matchers}

// TODO: replace this example test with your own, this is just here to demonstrate usage.
// See http://www.scalatest.org/at_a_glance for example usages
class DeodorantEvaporatorSpec extends AnyFlatSpec with Matchers {
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

class DeodorantEvaporatorScalaTest {
  @ParameterizedTest
  @MethodSource(Array("getInputData"))
  def shouldCalculateEvaporation(
      content: Int,
      evapPerDay: Int,
      threshold: Int,
      expectedResult: Int
  ) = {
    assertEquals(Sol.evaporator(content, evapPerDay, threshold), expectedResult)
  }
}
object DeodorantEvaporatorScalaTest {
  def getInputData(): java.util.stream.Stream[Arguments] = {
    java.util.stream.Stream.of(
      of(10, 10, 10, 22),
      of(10, 10, 5, 29),
      of(100, 5, 10, 59)
    )
  }
}
