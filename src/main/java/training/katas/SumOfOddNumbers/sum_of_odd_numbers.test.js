// Test.assertEquals(rowSumOddNumbers(1), 1);
// Test.assertEquals(rowSumOddNumbers(42), 74088);

const chai = require("chai");
const rowSumOddNumbers = require("./sum_of_odd_numbers").rowSumOddNumbers;
const assert = require("assert");
chai.config.truncateThreshold = 0;
const expect = require("chai").expect;

describe("Sum of odd numbers tests", function() {
    it("Tests", function() {
        assert.strictEqual(rowSumOddNumbers(1), 1);
        assert.strictEqual(rowSumOddNumbers(42), 74088);
    });
});
test("1-> 1", () => {
    expect(rowSumOddNumbers(1)).to.equal(1);
});
test("42-> 74088", () => {
    expect(rowSumOddNumbers(42)).to.equal(74088);
});