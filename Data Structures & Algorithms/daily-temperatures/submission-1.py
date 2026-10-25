class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #return list
        #result[i] 
        #num of days after ith day before a warmer temp
        stack = []
        result = [0] * (len(temperatures))
        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                x, y = stack.pop()
                result[x] = i-x
            stack.append((i,t))
        return result

