class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()

        while n not in s:
            s.add(n)

            r = 0
            while n:
                x = n % 10
                r += x ** 2
                n //= 10

            n = r

        return n == 1 








