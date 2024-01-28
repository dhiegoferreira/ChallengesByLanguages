using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace CodilityChallenges
{
    public class TestPDFQT5B79
    {

        public static int Problem(int[] A)
        {
            //Validations
            if (A.Length < 1 || A.Length > 1000000000)
                return 0;

            foreach(int i in A)
            {
                if (i <= 1 && i >= 100000)
                    return 0;
            }


            int highestOdd = 0;
            int highestEven = 0;


            for (int i = 0; i < A.Length; i++)
            {
                int n = (A[i] + 1) % 2;
                if (A[i] > highestOdd && n == 0)
                {
                    highestOdd = A[i];
                } else if (A[i] > highestEven && n != 0) //isn´t odd
                {
                    highestEven = A[i];
                }
            }

            if (highestEven <= 0)
                return highestOdd;



            return highestOdd + highestEven;
            



        }



    }
}
