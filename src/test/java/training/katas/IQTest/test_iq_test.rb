describe "Basic tests" do
  it "should pass basic tests" do
    Test.assert_equals(iq_test("2 4 7 8 10"),3)
    Test.assert_equals(iq_test("1 2 2"), 1)
  end
end