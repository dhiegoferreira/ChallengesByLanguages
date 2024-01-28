using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace CodilityChallenges
{
    public class CyclingRotation
    {

        public static int[] CyclingRotationSet(int[] A, int K)
        {

            //Validations
            if(A.Length <= 0 || A.Length > 100)
                return null;

            if (K < 0 || K > 100)
                return null;

          
            foreach(int num in A)
            {
                if (num <= -1000 && num >= 1000)
                    return null;
            }

            int count = 0;
            
            while(count != K)
            {
                int lastNumber = A[A.Length - 1];
                for(int i = A.Length - 1; i >= 1; i--)
                {
                    A[i] = A[i - 1];
                }
                A[0] = lastNumber;
                count++;
            }


            return A;

        }





    }
}
