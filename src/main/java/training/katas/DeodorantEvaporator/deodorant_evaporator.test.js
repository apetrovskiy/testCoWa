// Test.assertEquals(evaporator(10,10,10),22);

const chai = require("chai");
const evaporator = require("./deodorant_evaporator").evaporator;
// const assert = chai.assert;
const assert = require("assert");
chai.config.truncateThreshold = 0;
const expect = require("chai").expect;

describe("Deodorant Evaporator tests", function() {
    it("Tests", function() {
        assert.strictEqual(evaporator(10, 10, 10), 22);
        assert.strictEqual(evaporator(10, 10, 5), 29);
        assert.strictEqual(evaporator(100, 5, 5), 59);
    });
});
test("10 10 10 -> 22", () => {
    expect(evaporator(10, 10, 10)).to.equal(22);
});
test("10 10 5 -> 29", () => {
    expect(evaporator(10, 10, 5)).to.equal(29);
});
test("100 5 5 -> 59", () => {
    expect(evaporator(100, 5, 5)).to.equal(59);
});