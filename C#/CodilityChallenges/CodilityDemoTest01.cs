using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace CodilityChallenges
{
    public class CodilityDemoTest01
    {
        public static int Task1(int[] A)
        {
            int smallestPositive;
            //validations 

            int highestValue = A.Max();
            int smallestValue = A.Min();
            int[] OrderedArray = new int[highestValue];

            for (int i = 0; i < highestValue; i++)
            {
                OrderedArray[i] = i;
                i++;
            }




            List<int> DotNotContain = new List<int>();

            foreach (int j in A)
            {
                if (OrderedArray.ToList().Contains(j) == false)
                    DotNotContain.Add(j);

            }


            if (DotNotContain.Count == 0)
            {
                return highestValue + 1;
            }
            else
            {
                return DotNotContain.Max() - 1;
            }


            //ordered







        }




    }
}
