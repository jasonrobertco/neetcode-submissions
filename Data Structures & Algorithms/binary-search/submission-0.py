class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #cut it in half and divide by 2 no remainder
        l = 0
        r = len(nums)-1
        
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m-1
            else:
                l = m+1
        return -1
                