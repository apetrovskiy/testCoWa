namespace training.katas.SplitStrings
{
    using System;
    using System.Linq;

    public class SplitString
    {
        public static string[] Solution(string str)
        {
            if (string.IsNullOrEmpty(str))
                return Array.Empty<string>();
            return Enumerable.Range(0, str.Length)
                .Where(index => index % 2 == 0)
                .Select(index => str.Substring(index, 1) + (index + 1 < str.Length ? str.Substring(index + 1, 1) : "_"))
                .ToList()
                .ToArray();
        }
    }
}