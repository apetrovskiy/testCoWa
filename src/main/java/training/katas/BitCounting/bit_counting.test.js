/*
const { assert } = require("chai")

describe("Basic tests", () => {
        it("Testing for fixed tests", () => {
            assert.strictEqual(countBits(0), 0);
            assert.strictEqual(countBits(4), 1);
            assert.strictEqual(countBits(7), 3);
            assert.strictEqual(countBits(9), 2);
            assert.strictEqual(countBits(10), 2);
        })
    })
*/

// const chai = require("chai");
const countBits = require("./bit_counting").countBits;
const { assert, expect } = require("chai")
    // chai.config.truncateThreshold = 0;
    // const expect = require("chai").expect;

describe("Bit Counting tests", function() {
    it("Tests", function() {
        assert.strictEqual(countBits(0), 0);
        assert.strictEqual(countBits(4), 1);
        assert.strictEqual(countBits(7), 3);
        assert.strictEqual(countBits(9), 2);
        assert.strictEqual(countBits(10), 2);
    });
});
test("0 -> 0", () => {
    expect(countBits(0)).to.equal(0);
});
test("4 -> 1", () => {
    expect(countBits(4)).to.equal(1);
});
test("7 -> 3", () => {
    expect(countBits(7)).to.equal(3);
});
test("9 -> 2", () => {
    expect(countBits(9)).to.equal(2);
});
test("10 -> 2", () => {
    expect(countBits(10)).to.equal(2);
});
test("4 -> 1", () => {
    expect(countBits(4)).to.equal(1);
});