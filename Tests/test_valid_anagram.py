import unittest

from Solutions.valid_anagram import Solution

class TestValidAnagram(unittest.TestCase):
    def setUp(self) -> None:
        self.str1 = "ab"
        self.str2 = "ba"
        self.str3 = "anagram"
        self.str4 = "nagaram"
        self.str5 = "rat"
        self.str6 = "car"

    def test_valid_anagram(self):
        self.assertEqual(Solution.is_anagram(self.str1, self.str2), True)
        self.assertEqual(Solution.is_anagram(self.str3, self.str4), True)

    def test_invalid_anagram(self):
        self.assertEqual(Solution.is_anagram(self.str5, self.str6), False)
        self.assertEqual(Solution.is_anagram(self.str3, self.str6), False)


if __name__ == '__main__':
    unittest.main()
