class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxprofit=0
        minprice=prices[0]
        for p in prices:
            if p<minprice:
                minprice=p
            else:
                maxprofit+=p-minprice
                minprice=p
        return maxprofit