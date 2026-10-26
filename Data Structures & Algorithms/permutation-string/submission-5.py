class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool: 
        sub = s1
        full = s2
        subcount = [0] * 26
        fullcount = [0] * 26
        L = 0
        for R in range(len(sub)):
            subcount[ord(sub[R]) - ord("a")] += 1
        for R in range(len(full)):
            fullcount[ord(full[R]) - ord("a")] += 1
            while (R-L+1) > len(sub):
                fullcount[ord(full[L]) - ord("a")] -= 1
                L +=1
            if fullcount == subcount:
                return True
        return False



        
        



        