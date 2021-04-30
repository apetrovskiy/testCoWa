// Test.assertEquals(evaporator(10,10,10),22);

// import { JasmineAllureReporter } from "allure-jasmine";
// import { AllureRuntime, Status, TestResult } from "allure-js-commons";
const chai = require("chai");
const pickPeaks = require('../deodorant_evaporator');
const assert = chai.assert;
chai.config.truncateThreshold = 0;

describe("Sample tests", function() {
it("Tests", function() {
    assert.equal(evaporator(10, 10, 10), 2);
    assert.equal(evaporator(10, 10, 5), 29);
    assert.equal(evaporator(100, 5, 5), 59);
});
});
});