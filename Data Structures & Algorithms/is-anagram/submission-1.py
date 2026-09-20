class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #care about frequency so set > hash
        mydict = {}
        mydict2 = {}
        for i, letter in enumerate(s):
            if letter in mydict:
                #dicts uses brackets[] not ()
                mydict[letter] += 1
            else:
                mydict[letter] = 1
        for i, letter in enumerate(t):
            if letter in mydict2:
                mydict2[letter] += 1
            else:
                mydict2[letter] = 1  
        return mydict == mydict2
