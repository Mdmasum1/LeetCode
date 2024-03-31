
from typing import List

class Solution:

                        
    #Memoization (Top-Down)
    #Time Complexity: O(n)
    #Space Complexity: O(n)

    def rob(self, nums: List[int]) -> int:
       
        memo = {}

        #Base
        if not nums:
            return 0

        #Helper function
        def helper(i): #i is tracking the current index

            #base case
            if i in memo:
                return memo[i]

            if i < 0:
                return 0
            
            #Recurrence relation(head + tail ) method
            plan = nums[i] + helper(i - 2)
            non_plan = 0 + helper(i - 1)

            memo[i] = max(plan, non_plan)

            return memo[i]

        #return for the wwhole array
        return helper(len(nums) - 1)
    
# create obj of the solution class
nums = [1, 2, 3, 1]
solution = Solution()
print(solution.rob(nums)) # Output will be the maximum amount money from robbery

