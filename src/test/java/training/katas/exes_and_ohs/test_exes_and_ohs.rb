require 'test/unit'
require 'rspec'
require 'rspec/autorun'
require './src/main/java/training/katas/exes_and_ohs/exes_and_ohs.rb'


RSpec.describe 'exes and ohs' do
  describe '#some_method_under_test' do
    subject { XO input }

    [
      ['xo', true],
      ['XO', true],
      ['xo0', true],
      ['xxxoo', false],
      ["xxOo", true]
    ].each do |input, expected_output|
      it "when the input is #{input}" do
        # let(:input_value) { input }
        actual_result = XO(input)
        expect(expected_output).to eql XO(input)
        expect(actual_result).to equal(expected_output)
        expect(actual_result).to be == expected_output
      end
    end
  end
end


=begin
Test.assert_equals(XO('xo'),true)
Test.assert_equals(XO('XO'),true)
Test.assert_equals(XO('xo0'),true)
Test.assert_equals(XO('xxxoo'),false)
Test.assert_equals(XO("xxOo"),true)
=end
