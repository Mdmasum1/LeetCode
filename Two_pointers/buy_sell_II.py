from typing import List

#Leet code 122

class Solution:

    def maxProfit(self, prices: List[int]) -> int:

        #Base case
        if not prices:
            return 0
        
        total_profit = 0

        l, r = 0, 1

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                total_profit += profit

            l = r

            r += 1

        return total_profit
    
nums = [7,1,5,3,6,4]
solution = Solution()
result = solution.maxProfit(nums)
print(result)   # result = 7






