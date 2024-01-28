using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CodilityChallenges
{
    public class FibonacciSequence
    {
        public static void GivenNumbersFibonacciSequence(int number)
        {

            //Fibonacci sequence is a sequence in which each numbers is the sum of the two proceding ones. Numbbers that are part of the Fibonacci sequence are known as Fibonacci numbers.

            //The sequence commonly starts from 0 and 1, although some authours start the sequence from 1 and 1 or sometimes from 1 and 2. 


            int a = 0;
            int b = 1;
            int c = 0;
            
            
            int count = 0;
            while (a <= number)
            {
                count++;
              
                Console.WriteLine(a);
                c = a + b;
                a = b;
                b = c;

                if (count == number)
                    break;
            }



        }

    }
}
