using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace pt_bac2
{
    class QuadraticEquation
    {
        static void Main()
        {
            double a, b, c;

            Console.Write("Nhập giá trị của a: ");
            a = double.Parse(Console.ReadLine());

            Console.Write("Nhập giá trị của b: ");
            b = double.Parse(Console.ReadLine());

            Console.Write("Nhập giá trị của c: ");
            c = double.Parse(Console.ReadLine());

            double delta = b * b - 4 * a * c;

            if (delta < 0)
            {
                Console.WriteLine("Phương trình vô nghiệm");
            }
            else if (delta == 0)
            {
                double x = -b / (2 * a);
                Console.WriteLine("Phương trình có nghiệm kép x = " + x);
            }
            else
            {
                double x1 = (-b + Math.Sqrt(delta)) / (2 * a);
                double x2 = (-b - Math.Sqrt(delta)) / (2 * a);
                Console.WriteLine("Phương trình có 2 nghiệm phân biệt: x1 = " + x1 + ", x2 = " + x2);
            }
            Console.ReadLine();
        }
    }


}
