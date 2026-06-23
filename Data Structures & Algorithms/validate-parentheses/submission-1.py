class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ['[','{','(']:
                stack.append(i)
            else:
                if stack:
                    if i==')':
                        if stack[-1] == '(':
                            stack.pop(-1)
                        else:
                            return False
                    elif i=='}':
                        if stack[-1] == '{':
                            stack.pop(-1)
                        else:
                            return False
                    elif i==']':
                        if stack[-1] == '[':
                            stack.pop(-1)
                        else:
                            return False
                else:
                    return False
        return len(stack) == 0