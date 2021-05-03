const pyramid = require("./pyramid_array").pyramid;
const { assert, expect } = require("chai")

describe('Pyramid array basic tests', () => {
    it("Testing for 0", () => assert.deepEqual(pyramid(0), []));
    it("Testing for 1", () => assert.deepEqual(pyramid(1), [
        [1]
    ]));
    it("Testing for 2", () => assert.deepEqual(pyramid(2), [
        [1],
        [1, 1]
    ]));
    it("Testing for 3", () => assert.deepEqual(pyramid(3), [
        [1],
        [1, 1],
        [1, 1, 1]
    ]));
});