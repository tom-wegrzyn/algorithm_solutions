class Solution:
    @staticmethod
    def isAnagram(s: str, t: str) -> bool:
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
