class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #index is number of times, value are list of numbers at that freq
        freq = [[] for i in range(len(nums) + 1)] #list for every possible num
        for n in nums:
            count[n] = 1 + count.get(n,0)
            #add to dict
            #coutn the number, number is index count is value
        for n,c in count.items(): 
            #items gives index, valueenumerate starts 0 index does nto care
            #add the number to freq based on count index
            freq[c].append(n)
        res = []
        for i in range(len(freq)-1,0,-1): #start end step
            for n in freq[i]: #skips empty
                res.append(n)
                if len(res) == k:
                    return res        