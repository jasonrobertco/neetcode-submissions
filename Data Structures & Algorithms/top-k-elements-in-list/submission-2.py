class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #im thinking we make a hashmap and ruetnr hte highest count
        # we only need as many buckest as the list to be optimal

        #buckets
        counts = {}
        freq = [[] for i in range(len(nums)+1)]
        
        #iterate thru list 
        for num in nums:
            #update the counts for each respective num
            counts[num] = counts.get(num,0) + 1
        #now that we hav ethe coutn of eahc respective num we need to loop thru count 
        for key, value in counts.items():
        #since its a lsit we need to append to the list and we append hte key
            freq[value].append(key)
        #search back from freq 
        answer = []
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res


            

