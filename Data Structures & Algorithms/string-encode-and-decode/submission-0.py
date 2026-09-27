class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
            #length + # + string
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        #list of strings, i is ptr

        while i < len(s):
            #2nd ptr
            j = i
            while s[j] != '#':
                #increment j
                j += 1
            #stos at x for :x
            length = int(s[i:j])
            #indices i to j ie how long string is
            #i would start at 0 and end before j
            res.append(s[j+1:j+1+length])
            #stops at length -1
            i = j + 1 + length
        return res

