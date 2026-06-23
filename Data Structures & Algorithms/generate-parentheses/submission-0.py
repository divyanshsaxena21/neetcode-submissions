class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def palind(s):
            stack = []
            for i in s:
                if i=='(':
                    stack.append(i)
                elif stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            return len(stack)==0
        def gen(n,s,res,op,cl):
            if len(s) == n*2:
                if palind(s):
                    res.append(s)
                
                return
            if op<n:    
                gen(n,s+'(',res,op+1,cl)
                # s
            if cl<op:
                gen(n,s+')',res,op,cl+1)
            # return res
        
        res = []
        gen(n,'',res,0,0)
        return res