puts 'bbb'
Test.assert_equals(XO('xo'),true)
Test.assert_equals(XO('XO'),true)
Test.assert_equals(XO('xo0'),true)
Test.assert_equals(XO('xxxoo'),false)
Test.assert_equals(XO("xxOo"),true)
