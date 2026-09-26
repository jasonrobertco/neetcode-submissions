class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            if char == ")":
                if not stack or stack[-1] != "(":
                    return False
                stack.pop()
            if char == "}":
                if not stack or stack[-1] != "{":
                    return False
                stack.pop()
            if char == "]":
                if not stack or stack[-1] != "[":
                    return False
                stack.pop()

        return not stack