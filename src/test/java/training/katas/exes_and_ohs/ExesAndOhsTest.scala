package training.katas.exes_and_ohs

import org.scalatest._

class ExesAndOhsTest extends FlatSpec with Matchers {

  val tests = List(
    ("xo", true),
    ("xo0", true),
    ("xxxoo", false)
  )

  tests.foreach {
    case (input, expected) =>
      s"xo($input)" should s"return $expected" in {
        ExesAndOhs.xo(input) should be (expected)
      }
  }
}
