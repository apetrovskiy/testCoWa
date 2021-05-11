package training.katas.exes_and_ohs

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
