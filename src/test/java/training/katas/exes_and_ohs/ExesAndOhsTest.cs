namespace training.katas.exes_and_ohs
{
    using NUnit.Framework;
    using System;

    [TestFixture]
    public class SolutionTest
    {
        [Test]
        public void ExesAndOhsTests()
        {
            Assert.AreEqual(true, Kata.XO("xo"));
            Assert.AreEqual(true, Kata.XO("xxOo"));
            Assert.AreEqual(false, Kata.XO("xxxm"));
            Assert.AreEqual(false, Kata.XO("Oo"));
            Assert.AreEqual(false, Kata.XO("ooom"));
        }
    }
}
