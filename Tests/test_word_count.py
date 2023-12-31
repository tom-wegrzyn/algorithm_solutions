import unittest

from Solutions.word_count import WordCount

class TestContainsDuplicate(unittest.TestCase):
    def setUp(self) -> None:
        self.fileName = "Test Word Count Text"

    def test_word_count(self):
        self.assertEqual(WordCount.get_info(WordCount, "-c", self.fileName), 34)
        self.assertEqual(WordCount.get_info(WordCount, "-l", self.fileName), 4)
        self.assertEqual(WordCount.get_info(WordCount, "-w", self.fileName), 5)
        self.assertEqual(WordCount.get_info(WordCount, "-m", self.fileName), 31)
        self.assertEqual(WordCount.get_info(WordCount, "", self.fileName), (34, 4, 5, 31))


if __name__ == '__main__':
    unittest.main()