class Solution:
    @staticmethod
    def isAnagram(s: str, t: str) -> bool:
        """
        Takes in two strings and determines if they are an anagram.

        Anagram: a word, phrase, or name formed by rearranging the letters of another,
        such as cinema, formed from iceman.

        Parameters
        ----------
        s : str
            The first string in the anagram comparison.
        t : str
            The second string in the anagram comparison.

        Returns
        ----------
        bool
            True or false depending on if the words are a valid anagram.
        """
        s, t = s.strip().lower(), t.strip().lower()
        letters = dict()
        for x in s:
            if x in letters:
                letters[x] += 1
            else:
                letters.update([(x, 1)])

        for x in t:
            if x in letters and letters[x] != 0:
                letters[x] -= 1
            else:
                return False

        return True
