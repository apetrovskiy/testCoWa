namespace training.katas.exes_and_ohs
{
    using System.Linq;
    using System;

    public static class Kata
    {
        public static bool XO(string input)
        {
            // return //Code it!
            var lowerCasedString = input.ToLower();
            var x = 'x';
            var o = 'o';
            return lowerCasedString
            .Where(i => i == x)
            .Count() == lowerCasedString
            .Where(i => i == o)
            .Count();
        }
    }
}
