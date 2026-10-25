class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #return list
        #result[i] 
        #num of days after ith day before a warmer temp
        stack = []
        result = [0] * (len(temperatures))
        for i, t in enumerate(temperatures):
            if stack:
                a, b = stack[-1]
                while b < t and stack:
                    x, y = stack.pop()
                    result[x] = i-x
                    if stack:
                        a, b = stack[-1]
            stack.append((i,t))
        return result

