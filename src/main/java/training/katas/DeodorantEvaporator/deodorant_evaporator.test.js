// Test.assertEquals(evaporator(10,10,10),22);

const chai = require("chai");
const evaporator = require("../deodorant_evaporator");
// const assert = chai.assert;
var assert = require("assert");
chai.config.truncateThreshold = 0;

describe("Deodorant Evaporator tests", function() {
    it("Tests", function() {
        // assert.equal(evaporator(10, 10, 10), 22);
        // assert.equal(evaporator(10, 10, 5), 29);
        // assert.equal(evaporator(100, 5, 5), 59);
        assert.strictEqual(evaporator(10, 10, 10), 22);
        assert.strictEqual(evaporator(10, 10, 5), 29);
        assert.strictEqual(evaporator(100, 5, 5), 59);
    });
});
test("10 10 10 -> 22", () => {
    expect(evaporator(10, 10, 10).toBe(22));
});
test("10 10 5 -> 29", () => {
    expect(evaporator(10, 10, 5).toBe(29));
});
test("100 5 5 -> 59", () => {
    expect(evaporator(100, 5, 5).toBe(+59));
});