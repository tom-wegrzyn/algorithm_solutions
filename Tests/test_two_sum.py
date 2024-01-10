import unittest

from Solutions.two_sum import Solution


class TestTwoSum(unittest.TestCase):
    def setUp(self) -> None:
        self.list1 = [2, 7, 11, 15]
        self.target1 = 9
        self.list2 = [3, 2, 4]
        self.target2 = 6
        self.list3 = [3, 3]
        self.target3 = 6

    def test_two_sum(self):
        self.assertEqual(Solution.two_sum(self.list1, self.target1), [0, 1])
        self.assertEqual(Solution.two_sum(self.list2, self.target2), [1, 2])
        self.assertEqual(Solution.two_sum(self.list3, self.target3), [0, 1])


if __name__ == '__main__':
    unittest.main()
