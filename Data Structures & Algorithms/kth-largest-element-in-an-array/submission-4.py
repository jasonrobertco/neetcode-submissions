class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #attempting to do quicksort but im stupid
        #partition at end
        k = len(nums) - k
        def quickSelect(l,r):
            post1 = l
            pivot = nums[r]
            for i in range(l,r):
                if nums[i] <= pivot:
                    nums[i], nums[post1] = nums[post1], nums[i]
                    post1 += 1
            nums[post1], nums[r] = nums[r], nums[post1]
            if post1 > k:
                return quickSelect(l, post1 - 1)
            elif post1 < k:
                return quickSelect(post1 + 1, r)
            else:
                return nums[post1]

        return quickSelect(0, len(nums) - 1)
            