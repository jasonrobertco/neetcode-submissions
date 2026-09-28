class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = len(numbers)-1
        while L < R:
            res = numbers[L] + numbers[R]
            if res == target:
                return [L+1, R+1]
            if res > target:
                R -= 1
            if res < target:
                L += 1
        
        