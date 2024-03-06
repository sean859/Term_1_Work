# Convert from C# to Python

"""public static int Square(int number)
{
     return number * number;
}"""

def Square(int):
    return int * int
# --------------------------------------------------------------------
"""public static string ConcatenateStrings(string str1, string str2)
{
    return str1 + str2;
}"""

def ConcatenateStrings(word1: str, word2: str):
    return word1 + word2
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
# -----------------------------------------------------------------
"""public static int SumArray(int[] numbers)
{
    return numbers.Sum();
}
public static void PrintMultiples(int n)"""

def SumArray(num1: int, num2: int):
    return num1 + num2
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
# ----------------------------------------------------------------
"""public static string GetDayOfWeek(int day)
{
    return Enum.GetName(typeof(DayOfWeek), day);
}"""

from datetime import datetime

def GetDayOfWeek():
    dt = datetime.now()
    x = dt.weekday()
    
    print('Datetime is:', dt)
    print('Day of week is:', x)
# ---------------------------------------------------------------
"""public static int FindMax(int[] numbers)
{
    return numbers.Max();
}"""

def FindMax(numlist: list):
    max_number = max(numlist)
    print(max_number)
# -------------------------------------------------------------
"""public static double CelsiusToFahrenheit(double celsius)
{
    return (celsius * 9 / 5) + 32;
}"""

def DoubleCelsiusToFahrenheit(double_celsius: int):
    new_amount = (double_celsius * 4.5) + 32
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
        return False
    else:
        return True
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
print(ReverseWords('This sentence is jut another test to make sure'))
