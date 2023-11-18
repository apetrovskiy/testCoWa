namespace training.katas.SplitStrings
{
    using NUnit.Allure.Core;
    using NUnit.Framework;

    [AllureNUnit]
    [TestFixture]
    public class SplitStringTests
    {
        [Test]
        public void BasicTests()
        {
            Assert.That(SplitString.Solution("abc"), Is.EqualTo(new string[] { "ab", "c_" }));
            Assert.That(SplitString.Solution("abcdef"), Is.EqualTo(new string[] { "ab", "cd", "ef" }));
        }
    }
}