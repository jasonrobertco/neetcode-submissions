class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range (len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]:
                    continue
            j = i + 1
            k = len(nums) -1
            while j < k:
                res = nums[j] + nums[k]
                if nums[i] + res == 0:
                    #add to answer
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                elif nums[i] + res < 0:
                    j += 1
                elif nums[i] + res > 0:
                    k -= 1
        return ans