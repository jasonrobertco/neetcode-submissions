class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #if hashmap already exists addd to bucket, else make a bucket
        #can I make a dict of dicts?
        mybuckets = dict()
        for word in strs:
            s_word = sorted(word)
            key = ''.join(s_word)
            if key in mybuckets:
                mybuckets[key].append(word)
            else:
                mybuckets[key] = [word]
        return list(mybuckets.values())
        