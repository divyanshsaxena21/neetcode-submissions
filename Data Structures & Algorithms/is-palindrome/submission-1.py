class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        res = ''
        for i in s:
            if i.isalnum() and i != ' ':
                res += i.lower()
        # print(res)
        # res.lower()
        return res == res[::-1]