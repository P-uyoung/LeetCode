class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = 0
        temp = float('inf')
        for p in prices[1:]:
            if p <= buy :
                if not sell:
                    buy = p
                    continue
                if p < temp:
                    temp = p
                    continue

            if p > sell - (buy-temp):
                buy = temp
                sell = p
       
            elif p > sell:
                buy = min(buy, temp)
                sell = p
                
        ans = sell-buy if sell-buy >= 0 else 0
                
        return ans