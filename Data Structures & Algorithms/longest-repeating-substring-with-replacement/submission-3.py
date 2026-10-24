class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #max len is 
        l = 0
        count = {}
        best = 0
        for i in range(len(s)):
            count[s[i]] = count.get(s[i],0) + 1
            maxf = max(count.values())
            while i-l+1-maxf > k:
                count[s[l]] -= 1
                l += 1
            best = max(best, i-l+1)
        return best


            

        