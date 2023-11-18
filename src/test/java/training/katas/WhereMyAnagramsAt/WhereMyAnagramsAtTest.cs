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
            Assert.That(Kata.Anagrams("a", new List<string> { "a", "b", "c", "d" }), Is.EqualTo(new List<string> { "a" }));
            Assert.That(Kata.Anagrams("racer", new List<string> { "carer", "arcre", "carre", "racrs", "racers", "arceer", "raccer", "carrer", "cerarr" }), Is.EqualTo(new List<string> { "carer", "arcre", "carre" }));
        }
    }
}