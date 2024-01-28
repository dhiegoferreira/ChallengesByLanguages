using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CodilityChallenges
{
    internal class BinaryGap
    {
        //Problem: Binary Gap
        //Short description: A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.
        //link: https://app.codility.com/programmers/lessons/1-iterations/binary_gap/

        public static int Main(int N)
        {
            //Console.WriteLine("Hello World");
         

            int resultDivision = 0;
            int remaining = 0;
            int lengthResultList = 0;



            StringBuilder resultOrderList = new StringBuilder();
            StringBuilder CorrectOrderList = new StringBuilder();
            StringBuilder AuxList = new StringBuilder();
            List<int> LengthsGaps = new List<int>();
            int countZeros = 0;

            //START CONVERT DECIMAL TO BINARY

            //N is an integer within the ange [1..2, 147, 483, 647]
            if (N < 1 && N > 999)
                return 0;
            do
            {
                remaining = N % 2;
                resultDivision = N / 2;
                N = resultDivision;
                if (resultDivision == 0)
                    resultOrderList.Append("1");
                else
                    resultOrderList.Append(remaining.ToString());


            } while (resultDivision != 0);


            string result = resultOrderList.ToString();

            lengthResultList = result.Length;

            for (int i = lengthResultList - 1; i >= 0; i--)
            {
                CorrectOrderList.Append(resultOrderList[i]);
            }
            //END CONVERT DECIMAL TO BINARY


            int lengthCorrectList = CorrectOrderList.ToString().Length;

            for (int i = 0; i < lengthCorrectList; i++)
            {
                if (CorrectOrderList[i].Equals('1'))
                {
                    AuxList.Append(CorrectOrderList[i]);
                    for (int j = i + 1; j < lengthCorrectList; j++)
                    {
                        if (CorrectOrderList[j].Equals('0'))
                        {
                            countZeros++;
                           
                        }
                        else if (countZeros >= 1 && CorrectOrderList[j].Equals('1'))
                        {
                            LengthsGaps.Add(countZeros);
                            countZeros = 0;
                            AuxList.Clear();
                            break;
                        }
                    }
                }
            }


            if (LengthsGaps.Count == 0)
                return 0;
            else
                return LengthsGaps.Max();

        }
    }
}
