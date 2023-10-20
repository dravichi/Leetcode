class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pointer = prices[0]
        res = 0
        for i in range(1, len(prices)):
            if prices[i] - pointer > res:
                res = prices[i] - pointer
            if prices[i] < pointer:
                pointer = prices[i]
        return res
        
