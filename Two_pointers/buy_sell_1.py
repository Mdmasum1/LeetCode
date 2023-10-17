
#Leet code 121:
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #Goal to return the maximum profit if not then return 0
        #if I use the brute force algorithm then the complexity with O(n2) which will not be 
        #efficient then apply sliding window will be more efficient(better complexity)
        

        #Intialize two pointers , max_profit variable(which will be return)

        l = 0
        r = 1

        max_profit = 0

        #Iterate through the every price of prices of the day
        while r < len(prices):

            #Find the present pattern
            current_profit = prices[r] - prices[l]

            # Checking the conditon and calculate the result
            if prices[l] < prices[r]:
                max_profit = max(current_profit, max_profit)

            else:  #update the left pointer
                l = r 

            #Then increment by 1 of the right pointer
            r += 1

        return max_profit

nums = [7,1,5,3,6,4]
solution = Solution()
result = solution.maxProfit(nums)
print(result)





