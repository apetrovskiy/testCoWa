// import { JasmineAllureReporter } from "allure-jasmine";
// import { AllureRuntime, Status, TestResult } from "allure-js-commons";
// Since Node 10, we're using Mocha.
// You can use `chai` for assertions.
const chai = require("chai");
const assert = chai.assert;
// Uncomment the following line to disable truncating failure messages for deep equals, do:
// chai.config.truncateThreshold = 0;
// Since Node 12, we no longer include assertions from our deprecated custom test framework by default.
// Uncomment the following to use the old assertions:
// const Test = require("@codewars/test-compat");
const anagrams = require("./where_my_anagrams_at").anagrams;

describe("Anagrams", function() {
    it("should test for something", function() {
        assert.strictEqual(anagrams("abba", ["aabb", "abcd", "bbaa", "dada"]), [
            "aabb",
            "bbaa",
        ]);
    });
});