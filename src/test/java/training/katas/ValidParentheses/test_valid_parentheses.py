from src.main.java.training.katas.ValidParentheses.valid_parentheses \
    import valid_parentheses
import pytest


test_data = [
    ("  (", False),
    (")test", False),
    ("", True),
    ("hi())(", False),
    ("hi(hi)()", True), ('(', False),
    (')', False),
    ('hi)(', False),
    ('hi(hi)(', False),
    ('((())()())', True),
    ('(c(b(a)))(d)', True),
    ('hi(hi))(', False),
    ('())(()', False),
    ('(x)(dq()p)(c)eomxfm', True)
]


@ pytest.mark.parametrize("input,expected_result", test_data)
def test_valid_parentheses(input: str, expected_result: bool):
    assert expected_result == valid_parentheses(input)


'''
Test.assert_equals(valid_parentheses("  ("),False)
Test.assert_equals(valid_parentheses(")test"),False)
Test.assert_equals(valid_parentheses(""),True)
Test.assert_equals(valid_parentheses("hi())("),False)
Test.assert_equals(valid_parentheses("hi(hi)()"),True)
'''
