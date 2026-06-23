class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
        for i in range(len(nums)):
            x = target - nums[i]
            if x in d and d[x] != i:
                # print(target-nums[i],i)
                return [i,d[x]]