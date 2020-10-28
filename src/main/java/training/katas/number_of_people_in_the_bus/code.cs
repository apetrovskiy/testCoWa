namespace trainig.katas.number_of_people_in_the_bus
{
    using System;
    using System.Collections.Generic;
    using System.Linq;

    public class Kata
    {
        public static int Number(List<int[]> peopleListInOut)
        {
            // Happy Coding

            return peopleListInOut.Select(item => item[0]).Sum() - peopleListInOut.Select(item => item[1]).Sum();
        }
    }
}
