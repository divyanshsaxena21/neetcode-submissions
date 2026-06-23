class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        if nums.count(0)>1:
            return [0]*len(nums)
        pro = 1
        zero = False
        for i in nums:
            if i == 0:
                zero = True
            else:
                pro *= i
        res = [0]*len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                res[i] = pro
            elif nums[i] != 0 and not zero:
                res[i] = pro//nums[i]
        return res