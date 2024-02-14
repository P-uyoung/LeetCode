class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = 0
        temp = float('inf')
        for p in prices[1:]:
            print(p, sell - (buy-temp), buy)
            if p <= buy :
                if not sell:
                    buy = p
                    continue
                if p < temp:
                    temp = p
                    continue

            if p > sell - (buy-temp):
                print("de")
                buy = temp
                sell = p
 
            
            elif p > sell:
                buy = min(buy, temp)
                sell = p
                
        print(sell, buy)
        ans = sell-buy if sell-buy >= 0 else 0
                
        return ans
            
                
            
        