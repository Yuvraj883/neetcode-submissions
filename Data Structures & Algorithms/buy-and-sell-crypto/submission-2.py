class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return -1
        
        maxProfit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                
                maxProfit = max(maxProfit, prices[j]-prices[i])
            
        
        return maxProfit