class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mydict = {}
        sub = {}
        L = 0
        #for c in range(len(s1))
        for c in s1:
            sub[c] = sub.get(c, 0) + 1
        for R in range(len(s2)):
            mydict[s2[R]] = mydict.get(s2[R], 0) + 1
            if R-L+1 > len(s1):
                #move L
                mydict[s2[L]] -= 1
                   
                if mydict[s2[L]] == 0:
                    del mydict[s2[L]]
                L += 1 
            if mydict == sub:
                    return True
            #move R
        return False
            

        
