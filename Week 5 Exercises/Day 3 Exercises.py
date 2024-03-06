# Convert from C# to Python

"""public static int Square(int number)
{
     return number * number;
}"""

def Square(int: int):
    return int * int
print(Square(17))
# --------------------------------------------------------------------
"""public static string ConcatenateStrings(string str1, string str2)
{
    return str1 + str2;
}"""

def ConcatenateStrings(word1: str, word2: str):
    return word1 + word2
print(ConcatenateStrings('Hello', 'World'))
# ---------------------------------------------------------------------
"""public static int CountVowels(string input)
{
    string vowels = "aeiouAEIOU";
    int count = 0;

    foreach (char character in input)
    {
        if (vowels.Contains(character))
        {
            count++;
        }
    }

    return count;
}"""

def CountVowels(input: str):
    vowels = 'aeiouAEIOU'
    count = 0

    for char in input:
        if char in vowels:
            count = count + 1
    return count
print(CountVowels('This should count the vowels of this sentence'))
# -----------------------------------------------------------------
"""public static int SumArray(int[] numbers)
{
    return numbers.Sum();
}
public static void PrintMultiples(int n)"""

def SumArray(num1: int, num2: int):
    return num1 + num2
print(SumArray(75,83))
# ----------------------------------------------------------------
"""public static void PrintMultiples(int n)
{
    for (int i = 1; i <= 5; i++)
    {
        Console.Write(n * i + " ");
    }
    Console.WriteLine();
}"""

def PrintMultiples(num: int):
    for i in range(1, 6):
        print(num * i)
        i = i + 1
PrintMultiples(75)
# ----------------------------------------------------------------
"""public static string GetDayOfWeek(int day)
{
    return Enum.GetName(typeof(DayOfWeek), day);
}"""

from datetime import datetime

def GetDayOfWeek():
    dt = datetime.now()
    x = dt.weekday() + 1
    days = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}
    for key, value in days.items():
        if x == value:
            currentday = key
    print(f'Today is {currentday}, with specific date being {dt}')
GetDayOfWeek()
# ---------------------------------------------------------------
"""public static int FindMax(int[] numbers)
{
    return numbers.Max();
}"""

def FindMax(numlist: list):
    max_number = max(numlist)
    print(max_number)
FindMax([3,6,1,54,23,76,84,53,7,92,3])
# -------------------------------------------------------------
"""public static double CelsiusToFahrenheit(double celsius)
{
    return (celsius * 9 / 5) + 32;
}"""

def DoubleCelsiusToFahrenheit(double_celsius: int):
    new_amount = double_celsius * 9/5 + 32
    return new_amount
print(DoubleCelsiusToFahrenheit(34))
# ------------------------------------------------------------
"""public static bool IsPrime(int number)
{
    if (number < 2) return false;
    for (int i = 2; i <= Math.Sqrt(number); i++)
    {
        if (number % i == 0) return false;
    }
    return true;
}"""

def IsPrime(num: int):
    if (num % 2)  == 0:
        return 'The Number Is Not A Prime Number'
    else:
        return 'The Number Is A Prime Number'
print(IsPrime(17))
# ----------------------------------------------------------
"""public static string ReverseWords(string sentence)
{
    string[] words = sentence.Split(' ');
    Array.Reverse(words);
    return string.Join(' ', words);
}"""

def ReverseWords(sentence: str):
    reversed_text = sentence[::-1]
    return reversed_text
print(ReverseWords('This sentence is just another test to make sure'))
# ------------------------------------------------------------------
"""using System;

class GreetingProgram
{
    static void Main()
    {
        Console.Write("Enter your name: ");
        string name = Console.ReadLine();

        Console.Write("Enter your age: ");
        int age = Convert.ToInt32(Console.ReadLine());

        Console.WriteLine($"Hello, {name}! You are {age} years old.");
    }
}"""

class GreetingProgram():
    def __init__(self) -> None:
        pass
    def main(self):
        name = input("Enter your name: ")
        age = input('Enter your age: ')
        print(f'Hello, {name}!, you are {age} years old.')
Me = GreetingProgram()
Me.main()
#----------------------------------------------------------------------------
"""using System;

class FactorialProgram
{
    static void Main()
    {
        Console.Write("Enter a number to calculate its factorial: ");
        int number = Convert.ToInt32(Console.ReadLine());

        long factorial = GetFactorial(number);

        Console.WriteLine($"The factorial of {number} is: {factorial}");
    }

    static long GetFactorial(int n)
    {
        if (n == 0 || n == 1)
        {
            return 1;
        }
        else
        {
            return n * GetFactorial(n - 1);
        }
    }
}"""

import math

class FactorialProgram():
    def __init__(self) -> None:
        pass
    def Main(self):
        n = int(input('Please enter the number of the factorial you want to find: '))
        print(f'Factorial: {math.factorial(n)}')
factnumber = FactorialProgram()
factnumber.Main()

