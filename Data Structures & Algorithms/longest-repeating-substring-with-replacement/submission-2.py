class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        maxf = 0
        res = 0
        count = {}
        for R in range(len(s)):
            count[s[R]] = count.get(s[R], 0) + 1
            maxf = max(maxf, count[s[R]])
            #while invalid
            while R-L+1 - maxf > k:
                count[s[L]] -= 1
                L += 1
            res = max(res, R-L+1)
        return res
        