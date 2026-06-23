class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        val = list(d.values())
        val.sort(reverse=True)
        res = []
        used_freq = set()
        i = 0
        while len(res) < k:
            freq = val[i]
            for key in d:
                if d[key] == freq and key not in res:
                    res.append(key)
                    if len(res) == k:
                        break
            i+= 1
        return res