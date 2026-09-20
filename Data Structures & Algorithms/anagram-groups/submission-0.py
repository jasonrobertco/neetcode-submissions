class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        #define tuple
        for i, word in enumerate(strs):
            count = [0] * 26 #26 elemnts
            for i, letter in enumerate(word):
                index = ord(letter) - ord('a')
                count[index] += 1
            key = tuple(count)  # immutable fingerprint for the word
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]
        return list(groups.values())
            
        