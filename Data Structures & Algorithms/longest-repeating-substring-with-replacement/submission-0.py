class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mydict = {}
        L = 0
        best = 0
        maxf = 0
        for R in range(len(s)): #move right array
            #expand R case
            mydict[s[R]] = mydict.get(s[R], 0) + 1
            #expand R case replace
            maxf = max(maxf, mydict[s[R]])    
            while R-L+1 - maxf > k:
                #expand L case
                mydict[s[L]] -= 1
                L += 1
            best = max(best, R-L+1)
        return best