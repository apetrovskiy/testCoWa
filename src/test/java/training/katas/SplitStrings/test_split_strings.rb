Test.assert_equals(solution("abcdef"), ["ab", "cd", "ef"])
Test.assert_equals(solution("abcdefg"), ["ab", "cd", "ef", "g_"])
Test.assert_equals(solution(""), [])

# TODO: Replace examples and use TDD by writing your own tests
# These are some of the methods available:
#   Test.expect(boolean, [optional] message)
#   Test.assert_equals(actual, expected, [optional] message)
#   Test.assert_not_equals(actual, expected, [optional] message)

describe "Solution" do
  it "should test for something" do
    Test.assert_equals("actual", "expected", "This is just an example of how you can write your own TDD tests")
  end
end
  