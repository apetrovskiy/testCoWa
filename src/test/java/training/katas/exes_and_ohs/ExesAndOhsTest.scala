package training.katas.exes_and_ohs

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.{Arguments, MethodSource}
import org.junit.jupiter.params.provider.Arguments.of
import org.scalatest.flatspec.AnyFlatSpec
import org.scalatest.matchers.should.Matchers

class ExesAndOhsTest extends AnyFlatSpec with Matchers {

  val tests = Seq(
    ("xo", true),
    ("xo0", true),
    ("xxxoo", false)
  )

  tests.foreach { case (input, expected) =>
    s"xo($input)" should s"return $expected" in {
      ExesAndOhs.xo(input) should be(expected)
    }
  }
}

class ExesAndOhsScalaTest {
  @ParameterizedTest
  @MethodSource(Array("getInputData"))
  def shouldCheckExesAndOhs(input: String, expectedResult: Boolean) = {
    assertEquals(ExesAndOhs.xo(input), expectedResult)
  }
}
object ExesAndOhsScalaTest {
  def getInputData(): java.util.stream.Stream[Arguments] = {
    java.util.stream.Stream.of(
      of("xo", true),
      of("xo0", true),
      of("xxxoo", false)
    )
  }
}
