class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        d = {}
        n = len(s)
        l,r = 0,0
        curr = 0
        while(r<n):
            if s[r] not in d or d[s[r]] < l:
                d[s[r]] = r
                r += 1
                res = max(res,r-l)
            else:
                l = max(l, d[s[r]] + 1)
                d[s[r]] = r
                r += 1
        return res