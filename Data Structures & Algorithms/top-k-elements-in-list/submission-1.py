class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #im thinking we make a hashmap and ruetnr hte highest count
        #make a dict
        mybuckets = {}
        answer = []
        #iterate thru list 
        for x in nums:
            #make a new bucket
            mybuckets[x] = mybuckets.get(x,0) + 1
            #do i have to sort it is ther a fucniton that just returnes the greates count?
        answer = sorted(mybuckets, key=mybuckets.get)
        return answer[-k:]

            

