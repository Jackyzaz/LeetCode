# Stack Structure

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        stack = [0]

        for i in range(0,len(s)):
            stack.append(s[i])
            if stack[-1] == ']' and stack[-2]== '[':
                stack.pop()
                stack.pop()
                continue

            if stack[-1] == '}' and stack[-2]== '{':
                stack.pop()
                stack.pop()
                continue

            if stack[-1] == ')' and stack[-2]== '(':
                stack.pop()
                stack.pop()
                continue

            # print(stack)

        if stack==[0]:
            return True
        else : return False