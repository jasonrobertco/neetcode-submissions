class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #in a list of numbers
        #can return output in any order
        counts = {}
        for n in nums:
            counts[n] = counts.get(n,0) + 1
        #build answer
        ordered = sorted(counts, key=counts.get, reverse=True)
        return ordered[:k]
        #sort keys
        