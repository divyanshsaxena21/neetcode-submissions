class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in '+-*/':
                stack.append(int(i))
            else:
                a = stack.pop()
                b = stack.pop()
                if i == '+':
                    res = b+a
                elif i=='-':
                    res = b-a
                elif i=='*':
                    res = b*a
                elif i =='/':
                    res = int(b/a)
                stack.append(res)
            print(stack)
        return stack[0]