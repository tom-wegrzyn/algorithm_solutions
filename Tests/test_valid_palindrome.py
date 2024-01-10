import pytest

from Solutions.valid_palindrome import valid_palindrome


class TestValidPalindrome:
    def test_valid_anagram(self) -> None:
        assert valid_palindrome("A man, a plan, a canal: Panama") == True
        assert valid_palindrome(" ") == True

    def test_invalid_anagram(self) -> None:
        assert valid_palindrome("race a car") == False


if __name__ == '__main__':
    pytest.main()
