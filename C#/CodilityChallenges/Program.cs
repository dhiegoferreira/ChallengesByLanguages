using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;

namespace CodilityChallenges
{
    internal class Program
    {
        static void Main(string[] args)
        {

            //int[] numbers = {};
            //numbers = CyclingRotation.CyclingRotationSet(numbers, 4); //Expectes 4,1,2,3

            //foreach(int number in numbers)
            //{
            //    Console.WriteLine(number);
            //}

            int[] A = { 1, 3, 6, 4, 1, 2 };
            //int[] A = { 1,2,3};
            //int[] A = { -1,-3};

            int result = CodilityDemoTest01.Task1(A);
            Console.WriteLine(result);

            Console.ReadLine();
        }
    }
}
