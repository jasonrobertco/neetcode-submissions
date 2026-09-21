class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mymap = defaultdict(list) #by default call list() which maes []
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')] += 1
            mymap[tuple(count)].append(s)
        return list(mymap.values())