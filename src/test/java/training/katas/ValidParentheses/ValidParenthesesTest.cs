namespace training.katas.ValidParentheses
{
    using NUnit.Allure.Core;
    using NUnit.Framework;
    using System;

    [AllureNUnit]
    [TestFixture]
    public class SolutionTest
    {
        [Ignore("TODO: no way of currently testing this")]
        [Test]
        public void SampleTest1()
        {
            Assert.AreEqual(true, Parentheses.ValidParentheses("()"));
        }

        [Test]
        public void SampleTest2()
        {
            Assert.AreEqual(false, Parentheses.ValidParentheses(")(((("));
        }
    }
}