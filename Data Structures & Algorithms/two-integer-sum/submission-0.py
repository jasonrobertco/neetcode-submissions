class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {} 
        #dont care about freq just if it exists
        for i, num in enumerate(nums):
            missing = target - num
            if missing in mydict:
                return [mydict[missing], i]
            mydict[num] = i 
            
        