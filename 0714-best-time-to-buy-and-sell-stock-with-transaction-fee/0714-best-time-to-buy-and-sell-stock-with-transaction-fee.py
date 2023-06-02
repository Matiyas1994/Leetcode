class Solution:
    def maxProfit(self, price: List[int], fee: int) -> int:
        @cache
        def dp(i, haveStock):
            if i==len(price):
                    return 0
            
            if haveStock:
                sell = dp(i+1, False) + price[i] - fee
                not_sell = dp(i+1, True)
                return max(sell, not_sell)
            else:
                buy = dp(i+1, True)- price[i]
                not_buy = dp(i+1, False)
                return max(buy, not_buy)
        return dp(0,False)