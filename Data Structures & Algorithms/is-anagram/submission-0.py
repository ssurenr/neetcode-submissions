from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        scount = Counter(s)
        tcount = Counter(t)

        for char, count in scount.items():
            if tcount[char] != count:
                return False
        return True