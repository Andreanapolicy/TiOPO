namespace Document
{
    class Program
    {
        public static void Main()
        {
            string test = "text";

            Console.WriteLine(test);

            changeString(ref test);

            Console.WriteLine(test);
        }

        public static void changeString(ref string text)
        {
            text = "text1";
        }
    }
}