class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myset = set()
        L = 0
        best = 0
        for R in range(len(s)):
            while s[R] in myset: #it sa duplicate
                myset.remove(s[L])
                L +=1
            myset.add(s[R])
            best = max(best, R-L+1)
        return best