class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        count = {}
        best = 0
        res = 0
        for R in range(len(s)):
            count[s[R]] = count.get(s[R], 0) + 1 #add to dict
            best = max(best, count[s[R]])
            while (R-L+1 - best) > k:
                count[s[L]] -= 1
                L += 1
            res = max(res, R-L+1)
        return res
                
