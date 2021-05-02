// Since Node 10, we're using Mocha.
// You can use `chai` for assertions.
const chai = require("chai");
const assert = chai.assert;
// Uncomment the following line to disable truncating failure messages for deep equals, do:
// chai.config.truncateThreshold = 0;
// Since Node 12, we no longer include assertions from our deprecated custom test framework by default.
// Uncomment the following to use the old assertions:
// const Test = require("@codewars/test-compat");
const evaporator = require("./nesting_structure_comparison");

describe("Nesting structure comparison", function() {
    it("should test for something", function() {
        // Test.assertEquals(1 + 1, 2);
        // assert.strictEqual(1 + 1, 2);
    });
});