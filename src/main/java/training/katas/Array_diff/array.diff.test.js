/*
describe("Sample tests", function() {
    it("Should pass Sample tests", function() {
        Test.assertDeepEquals(arrayDiff([], [4, 5]), [], "a was [], b was [4,5]");
        Test.assertDeepEquals(arrayDiff([3, 4], [3]), [4], "a was [3,4], b was [3]");
        Test.assertDeepEquals(arrayDiff([1, 8, 2], []), [1, 8, 2], "a was [1,8,2], b was []");
        Test.assertDeepEquals(arrayDiff([1, 2, 3], [1, 2]), [3], "a was [1,2,3], b was [1,2]")
    });
});
*/

const arrayDiff = require("./array.diff").arrayDiff;
const { assert, expect } = require("chai");

describe("Array diff tests", function() {
    it("Tests", function() {
        assert.deepEqual(arrayDiff([], [4, 5]), []);
        assert.deepEqual(arrayDiff([3, 4], [3]), [4]);
        assert.deepEqual(arrayDiff([1, 8, 2], []), [1, 8, 2]);
        assert.deepEqual(arrayDiff([1, 2, 3], [1, 2]), [3]);
    });
});
test("[], [4, 5] -> []", () => {
    expect(arrayDiff([], [4, 5])).to.equal([]);
});
test("[3, 4], [3] -> [4]", () => {
    expect(arrayDiff([3, 4], [3])).to.equal([4]);
});
test("[1, 8, 2], [] -> [1, 8, 2]", () => {
    expect(arrayDiff([1, 8, 2], [])).to.equal([1, 8, 2]);
});
test("[1, 2, 3], [1, 2] -> [3]", () => {
    expect(arrayDiff([1, 2, 3], [1, 2])).to.equal([3]);
});