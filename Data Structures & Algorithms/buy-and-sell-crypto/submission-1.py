class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        d = {}
        n = len(prices)
        for i in range(n):
            for j in range(i+1,n):
                if prices[j]>prices[i]:
                    if prices[i] in d:    
                        d[prices[i]] = max(d[prices[i]],prices[j])
                    else:
                        d[prices[i]] = prices[j]
        # print(d)
        if not d:        
            return 0
        max_profit = 0
        for i in d:
            max_profit = max(max_profit,d[i]-i)
        return max_profit