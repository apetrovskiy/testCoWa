namespace training.katas.WhereMyAnagramsAt
{
    using NUnit.Allure.Core;
    using NUnit.Framework;
    using System;
    using System.Collections.Generic;

    [AllureNUnit]
    [TestFixture]
    public class SolutionTest
    {
        [Ignore("TODO: no way of currently testing this")]
        [Test]
        public void SampleTest()
        {
            Assert.AreEqual(new List<string> { "a" }, Kata.Anagrams("a", new List<string> { "a", "b", "c", "d" }));
            Assert.AreEqual(new List<string> { "carer", "arcre", "carre" }, Kata.Anagrams("racer", new List<string> { "carer", "arcre", "carre", "racrs", "racers", "arceer", "raccer", "carrer", "cerarr" }));
        }
    }
}