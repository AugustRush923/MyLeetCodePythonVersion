import unittest
import roman_to_int


class TestRomanToInt(unittest.TestCase):
    def test_solution1(self):
        self.assertEqual(roman_to_int.my_solution1("III"), 3)
        self.assertEqual(roman_to_int.my_solution1("IV"), 4)
        self.assertEqual(roman_to_int.my_solution1("IX"), 9)
        self.assertEqual(roman_to_int.my_solution1("LVIII"), 58)  # L = 50, V= 5, III = 3.
        self.assertEqual(roman_to_int.my_solution1("MCMXCIV"), 1994)  # M = 1000, CM = 900, XC = 90, IV = 4.
        self.assertEqual(roman_to_int.my_solution1("MCDXCIX"), 1499)  # M = 1000, CD = 400, XC = 90, IX = 9.
        self.assertEqual(roman_to_int.my_solution1("XLI"), 41)


if __name__ == '__main__':
    unittest.main()
