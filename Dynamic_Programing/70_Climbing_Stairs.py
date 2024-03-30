
class Solution:
    '''
    Date: 3/29/2024. 
      problem: You are climbing a staircase. It takes n steps to reach the top.

      Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

      Example 1:

    Input: n = 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps

    '''

    def climbStairs(self, n: int) -> int:

        memo = {}  #Assign empty dictionary
        if n in memo:
            return memo[n]

        #Base case
        if n == 1 or n == 0:
            return 1 # when stairs 1 or 0 then you can top only one way

        #Topological sort increasing the loop
        for i in range(n):
            memo[n] = self.climbStairs(n - 1) + self.climbStairs(n -2)

        return memo[n]


# create obj of the solution class
solution = Solution()
print(solution.climbStairs(5))  # Output will be the number of ways to climb 5 stairs

