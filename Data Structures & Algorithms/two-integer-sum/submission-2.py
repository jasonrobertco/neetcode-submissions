class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums): #gives index i and value num
            comp = target - num
            if comp in hashmap:
                return [hashmap[comp], i]
            hashmap[num] = i
        return []
        