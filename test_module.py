import unittest
from main import *

def is_Ascending(lst):
    result = []
    for i in range(len(lst)-1):
        result.append(lst[i] <= lst[i+1])
    return all(result)
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

class TestAscending(unittest.TestCase):
    def test_is_Ascending(self):
        lis1 = [1,2,3,4,5,6,7,9]
        lis2 = [-2,-1,1,1,2,2,3,4]
        lis3 = [1,2,1,3,4,5,6,7]
        print(is_Ascending(lis3))
        self.assertTrue(is_Ascending(lis1),"List is ascending")
        self.assertTrue(is_Ascending(lis2),"List is ascending")
        self.assertFalse(is_Ascending(lis3),"List is not ascending")
    
    def test_is_Descending(self):
        lis1 = [7,6,5,4,3,2,1,0]
        lis2 = [7,7,6,6,5,5,4,3]
        lis3 = [7,10,6,5,4,3,2,1]
        self.assertFalse(is_Ascending(lis1),"List is descending")
        self.assertFalse(is_Ascending(lis2),"List is descending")
        self.assertFalse(is_Ascending(lis3),"List is not descending")
    
if __name__ == '__main__':
    unittest.main()