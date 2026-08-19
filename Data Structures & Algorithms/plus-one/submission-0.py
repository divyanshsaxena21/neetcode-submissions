class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in digits:
            num = (num*10) + i
        
        num += 1

        res = []
        while (num):
            res.append(num%10)
            num //= 10
        
        return res[::-1]