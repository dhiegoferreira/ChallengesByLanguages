using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CodilityChallenges
{
    public class Test2
    {
        public static int Problem(string S)
        {
            //Validations

            foreach (char s in S)
            {
                char letter = Convert.ToChar(s);
                if (Char.IsLetter(letter) == false || Char.IsUpper(letter) == false)
                    return 0;
            }


            int countA = 0;
            int countN = 0;
            int countB = 0;


            foreach (char s in S)
            {
                if (s.Equals('B'))
                    countB++;
                else if (s.Equals('A'))
                    countA++;
                else if (s.Equals('N'))
                    countN++;

            }


            if (countA % 3 == 0 && countB % 1 == 0 && countN % 2 == 0)
            {
                int sum = countA + countB + countN;
                return sum / 6;
            }
            else
            {
                return 0;
            }


        }

    }
}
