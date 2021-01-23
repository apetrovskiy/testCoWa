require 'test/unit'
require 'rspec'
require 'rspec/autorun'
require './src/main/java/training/katas/number_of_people_in_the_bus/number_of_people_in_the_bus.rb'


RSpec.describe 'number of people' do
  describe '#some_method_under_test' do
    subject { number input }

    [
      [[[10, 0], [3, 5], [5, 8]], 5],
      [[[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]], 17],
      [[[3, 0], [9, 1], [4, 8], [12, 2], [6, 1], [7, 8]], 21]
    ].each do |input, expected_output|
      it "when the input is #{input}" do
        # let(:input_value) { input }
        actual_result = number(input)
        expect(expected_output).to eql number(input)
        expect(actual_result).to equal(expected_output)
        expect(actual_result).to be == expected_output
      end
    end
  end
end
