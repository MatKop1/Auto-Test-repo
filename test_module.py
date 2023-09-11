import unittest
from main import *

class TestModule(unittest.TestCase):
    def test_Palindrome(self):
        Sol = Solution() 
        self.assertEqual(Sol.isPalindrome("A man, a plan, a canal: Panama"),True)
        self.assertEqual(Sol.isPalindrome("race a car"),False)
        self.assertEqual(Sol.isPalindrome(" ") ,True)

    def test_Solution(self):
        Sol = Solution() 
        self.assertEqual(Sol.isPalindrome("A man, a plan, a canal: Panama"),True)
        self.assertEqual(Sol.isPalindrome("race a car"),False)
        self.assertEqual(Sol.isPalindrome(" ") ,True)


if __name__ == '__main__':
    unittest.main()