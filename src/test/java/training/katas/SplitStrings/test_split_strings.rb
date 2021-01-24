require 'test/unit'
require 'rspec'
require 'rspec/autorun'
require './src/main/java/training/katas/SplitStrings/split_strings.rb'

=begin
Test.assert_equals(solution("abcdef"), ["ab", "cd", "ef"])
Test.assert_equals(solution("abcdefg"), ["ab", "cd", "ef", "g_"])
Test.assert_equals(solution(""), [])
=end

# TODO: Replace examples and use TDD by writing your own tests
# These are some of the methods available:
#   Test.expect(boolean, [optional] message)
#   Test.assert_equals(actual, expected, [optional] message)
#   Test.assert_not_equals(actual, expected, [optional] message)

RSpec.describe 'split strings' do
  describe '#some_method_under_test' do
    subject { solution input }

    [
      ['abc', ['ab', 'c_']],
      ['abcdef', ['ab', 'cd', 'ef']],
      ["asdfadsf", ['as', 'df', 'ad', 'sf']],
      ["asdfads", ['as', 'df', 'ad', 's_']],
      ["", []],
      ["x", ["x_"]],
      ["ulnckdcoygljbbkrjxmxmdxafyippuflgwaquathcrswadnbjglszozwtarkjtuojnamzzntnxpznjyrmjlskkkwmuzgyyxkju", ['ul', 'nc', 'kd', 'co', 'yg', 'lj', 'bb', 'kr', 'jx', 'mx', 'md', 'xa', 'fy', 'ip', 'pu', 'fl','gw', 'aq', 'ua', 'th', 'cr', 'sw', 'ad', 'nb', 'jg', 'ls', 'zo', 'zw', 'ta', 'rk', 'jt', 'uo', 'jn', 'am', 'zz', 'nt', 'nx', 'pz', 'nj', 'yr', 'mj', 'ls', 'kk', 'kw', 'mu', 'zg', 'yy', 'xk', 'ju']],
      ["whugsw", ['wh', 'ug', 'sw']]
    ].each do |input, expected_output|
      it "when the input is #{input}" do
        # let(:input_value) { input }
        actual_result = solution(input)
        expect(expected_output).to eql solution(input)
        expect(actual_result).to be == expected_output
      end
    end
  end
end
