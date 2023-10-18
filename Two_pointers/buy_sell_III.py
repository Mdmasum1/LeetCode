
from typing import List

#Leet code 123

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        
        #Base case
        if n <= 1:
            return 0

        maxprofit = 0

        left, right = 0, 0

        #Initialize two pairs of variables to keep track of buy and sell
        buy1, sell1, buy2, sell2 = float('inf'), 0, float('inf'), 0

        while right < len(prices):

            #Storing right pointer of present value from prices list to the price
            price = prices[right]

            #Checking all condtions
            #First buy (left pointer )
            buy1 = min(buy1, price)

            #First sell (right pointer tp get profit)
            sell1 = max(sell1, price - buy1)


            #Second buy (left pointer ,using profit from the first tramsaction )
            buy2 = min(buy2, price - sell1)

            #Second sell2(right pointer)
            sell2 = max(sell2, price - buy2)

            #Move the right pointer to the right
            right += 1


            #Update the maxProfit
            maxprofit = max(maxprofit, sell2)

        
        return maxprofit
    

nums = [3,3,5,0,0,3,1,4]
solution = Solution()
result = solution.maxProfit(nums)
print(result)   # result = 6



        