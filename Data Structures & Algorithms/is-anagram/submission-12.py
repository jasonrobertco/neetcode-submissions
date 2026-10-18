class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = [0] * 26
        for i in s: #for every char in str
            counts[ord(i)-ord("a")] += 1
        for i in t:
            counts[ord(i)-ord("a")] -= 1
        for i in counts:
            if i != 0:
                return False
        return True

        