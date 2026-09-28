class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        R = 0                      # changed: was 1
        best = 0
        bestset = set()            # moved: out of the loop
        while R < len(s):
            if s[R] in bestset:
                bestset.remove(s[L])   # changed: was L = R; R = L+1
                L += 1
            else:
                bestset.add(s[R])
                best = max(best, R - L + 1)   # changed: was R-L
                R += 1
        return best