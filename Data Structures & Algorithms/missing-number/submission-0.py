class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = 0
        for i in nums:
            if i!=s:
                return s
            s += 1