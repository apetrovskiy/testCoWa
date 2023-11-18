namespace training.katas.exes_and_ohs
{
    using NUnit.Allure.Core;
    using NUnit.Framework;
    using System;

    [AllureNUnit]
    [TestFixture]
    public class SolutionTest
    {
        [Test]
        public void ExesAndOhsTests()
        {
            Assert.That(Kata.XO("xo"), Is.EqualTo(true));
            Assert.That(Kata.XO("xxOo"), Is.EqualTo(true));
            Assert.That(Kata.XO("xxxm"), Is.EqualTo(false));
            Assert.That(Kata.XO("Oo"), Is.EqualTo(false));
            Assert.That(Kata.XO("ooom"), Is.EqualTo(false));
        }
    }
}
