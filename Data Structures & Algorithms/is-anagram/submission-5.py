class Solution:
    def isAnagram(self, s: str, t: str) -> bool: #s is a stirng t is a string
        if len(s) != len(t):
            return False
        mydict = {}
        for x in s:
            #hashmap
            mydict[x] = mydict.get(x, 0) + 1
            #mydict.get(key, default)
        for y in t:
            if y not in mydict:
                return False
            mydict[y] = mydict[y] - 1
            if mydict[y] == 0:
                del mydict[y]
        return True
            
            
            


