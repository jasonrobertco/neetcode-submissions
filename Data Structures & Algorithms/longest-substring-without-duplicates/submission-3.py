class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        myset = set()
        best = 0
        for R in range(len(s)):
            while s[R] in myset:
                myset.remove(s[L])
                L += 1
            else:
                myset.add(s[R])
                best = max(best, R-L+1)
        return best