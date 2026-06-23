class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        l = min(nums)
        m = max(nums)
        res = 0
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = i 
        curr = 0
        # print(d)
        while(l<=m):
            if l in d:
                curr += 1
            else:
                res = max(res,curr)
                curr = 0
            # print(curr,l)
            
            l += 1
        res = max(res,curr)
        return res