const chai = require("chai");
const pickPeaks = require('./pick_peaks').pickPeaks;
const assert = chai.assert;
chai.config.truncateThreshold = 0;

describe("Pick peaks", function() {
    it("Tests", function() {
        assert.deepEqual(pickPeaks([1, 2, 3, 6, 4, 1, 2, 3, 2, 1]), { pos: [3, 7], peaks: [6, 3] });
        assert.deepEqual(pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]), { pos: [3, 7], peaks: [6, 3] });
        assert.deepEqual(pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 2, 2, 1]), { pos: [3, 7, 10], peaks: [6, 3, 2] });
        assert.deepEqual(pickPeaks([2, 1, 3, 1, 2, 2, 2, 2, 1]), { pos: [2, 4], peaks: [3, 2] });
        assert.deepEqual(pickPeaks([2, 1, 3, 1, 2, 2, 2, 2]), { pos: [2], peaks: [3] });
        assert.deepEqual(pickPeaks([2, 1, 3, 2, 2, 2, 2, 5, 6]), { pos: [2], peaks: [3] });
        assert.deepEqual(pickPeaks([2, 1, 3, 2, 2, 2, 2, 1]), { pos: [2], peaks: [3] });
        assert.deepEqual(pickPeaks([1, 2, 5, 4, 3, 2, 3, 6, 4, 1, 2, 3, 3, 4, 5, 3, 2, 1, 2, 3, 5, 5, 4, 3]), { pos: [2, 7, 14, 20], peaks: [5, 6, 5, 5] });
        assert.deepEqual(pickPeaks([]), { pos: [], peaks: [] });
        assert.deepEqual(pickPeaks([1, 1, 1, 1]), { pos: [], peaks: [] });
    });
});