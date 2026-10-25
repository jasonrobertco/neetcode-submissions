class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {} #key:value 
        L = 0
        best = 0
        maxf = 0
        for R, c in enumerate(s):
            counts[c] = counts.get(c, 0) + 1
            maxf = max(maxf, counts[c])
            while (R-L+1) - maxf > k:
                counts[s[L]] -= 1
                L += 1
            best = max(best, R-L+1)
        
        return best

        