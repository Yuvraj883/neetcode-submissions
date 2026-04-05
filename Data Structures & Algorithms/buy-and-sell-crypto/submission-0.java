class Solution {
    public int maxProfit(int[] prices) {
        if(prices.length<=1){
            return 0; 
        }
        int maxProfit = 0; 
        
        for(int i=0; i<prices.length; i++){
            int profit = 0;
            for(int j=i+1; j<prices.length; j++){
                profit = prices[j]-prices[i]; 
                maxProfit = Math.max(maxProfit, profit);
            }
        }

        return maxProfit;

    }
}
