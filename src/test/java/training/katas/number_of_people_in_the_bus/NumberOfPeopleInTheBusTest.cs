namespace training.katas.number_of_people_in_the_bus
{
    using NUnit.Allure.Core;
    using NUnit.Framework;
    using System;
    using System.Collections.Generic;

    [AllureNUnit]
    [TestFixture]
    public class MyTest
    {
        [Test]
        public void FirstTest()
        {
            List<int[]> peopleList = new List<int[]>() { new[] { 10, 0 }, new[] { 3, 5 }, new[] { 5, 8 } };
            Assert.That(Kata.Number(peopleList), Is.EqualTo(5));
        }
        [Test]
        public void SecondTest()
        {
            List<int[]> peopleList = new List<int[]>() { new[] { 3, 0 }, new[] { 9, 1 }, new[] { 4, 10 }, new[] { 12, 2 }, new[] { 6, 1 }, new[] { 7, 10 } };
            Assert.That(Kata.Number(peopleList), Is.EqualTo(17));
        }
        [Test]
        public void ThirdTest()
        {
            List<int[]> peopleList = new List<int[]>() { new[] { 3, 0 }, new[] { 9, 1 }, new[] { 4, 8 }, new[] { 12, 2 }, new[] { 6, 1 }, new[] { 7, 8 } };
            Assert.That(Kata.Number(peopleList), Is.EqualTo(21));
        }
    }
}
