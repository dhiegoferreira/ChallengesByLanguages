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

            //int[] A = { 1, 3, 6, 4, 1, 2 };
            //int[] A = { 1,2,3};
            //int[] A = { -1,-3};

            //int result = CodilityDemoTest01.Task1(A);


            //int[] A = { 5, 3, 10, 6, 11 };
            //int[] A = { 20, 10, 7, 5};
            //int[] A = { 7, 13, 15, 13 };
            //int[] A = { 2,6,4,6 };

            //int result = TestPDFQT5B79.Problem(A);


            string A = "NAANAAXNABABYNNBZ";
            //string[] A = { "NAANAAXNABABYNNBZ" };

            int result = Test2.Problem(A);

            Console.WriteLine(result);

            Console.ReadLine();
        }
    }
}
