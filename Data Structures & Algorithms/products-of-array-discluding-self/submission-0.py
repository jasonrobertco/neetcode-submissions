class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #input is array/list nums of numbers
        #return output of product of everything except i
        #could u solve without using division?
        #create an output
        #proucct of index to the left
        out = [1] * len(nums)        
        left = 1
        # first pass: left -> right
        # at index i, left equals product of nums[0..i-1]
        for i in range(len(nums)):
            out[i] = left          # store product of elements before i
            left *= nums[i]        # update left to include nums[i]
        right = 1

        # second pass: right -> left
        # at index i, right equals product of nums[i+1..end]
        for i in range(len(nums) - 1, -1, -1):
            out[i] *= right        # multiply product of elements after i
            right *= nums[i]       # update right to include nums[i]
        return out
        

