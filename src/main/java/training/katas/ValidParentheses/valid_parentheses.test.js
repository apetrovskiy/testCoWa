/*
Test.assertEquals(validParentheses("()"), true);
Test.assertEquals(validParentheses("())"), false);
*/

const chai = require("chai");
const assert = chai.assert;
const validParentheses = require("./valid_parentheses").validParentheses;

describe("Valid parentheses", function() {
    it("should test for something", function() {
        assert.strictEqual(validParentheses(""), true);
    });
});