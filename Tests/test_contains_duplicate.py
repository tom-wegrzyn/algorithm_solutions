import unittest

from Solutions.contains_duplicate import Solution

class TestContainsDuplicate(unittest.TestCase):
    def setUp(self) -> None:
        self.list1 = [0, 1, 2, 4, 5, 6, 7, 8, 9, 4, 10]
        self.list2 = [0]
        self.list3 = [1, 4, 8, 3, 6, 7]

    def test_contains_duplicate1(self):
        self.assertEqual(Solution.containsDuplicateFirstIteration(Solution, self.list1), True)
        self.assertEqual(Solution.containsDuplicateFirstIteration(Solution, self.list2), False)
        self.assertEqual(Solution.containsDuplicateFirstIteration(Solution, self.list3), False)

    def test_contains_duplicate2(self):
        self.assertEqual(Solution.containsDuplicateSecondIteration(self.list1), True)
        self.assertEqual(Solution.containsDuplicateSecondIteration(self.list2), False)
        self.assertEqual(Solution.containsDuplicateSecondIteration(self.list3), False)


if __name__ == '__main__':
    unittest.main()
