class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() #modifies nums to be sorted
        # i + j + k = 0
        for i, n in enumerate(nums):
            if n > 0:
                break #this skips all the positive values
                #because n must be negative for sum == 0
            if i > 0 and n == nums[i-1]: #protect -1 index
                continue
            l = i+1
            r = len(nums)-1
            
            while l < r:
                tot = n + nums[l] + nums[r]
                if tot > 0:
                    r -= 1
                elif tot < 0:
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res