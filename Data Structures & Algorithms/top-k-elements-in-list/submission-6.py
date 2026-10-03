class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        res = []
        for num in nums: #ints
            count[num] = count.get(num, 0) + 1
        for key, value in count.items():
            #items gives k,v
            #values gives v
            #nums gives k
            freq[value].append(key)
        for i in range(len(freq)-1, 0, -1): #start stop step
            for item in freq[i]:
                res.append(item)
                if len(res) == k:
                    return res
                

