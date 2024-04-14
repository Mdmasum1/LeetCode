'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

'''

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        #initialize the empty result array
        res = []

        #Sorting the input
        nums.sort()

        n = len(nums)

        for i in range(n -3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range (i + 1, n -2):
                #Corner case
                if j > i + 1 and nums[j] == nums[j -1]:
                    continue

                #Initialize left and right pointers
                l , r = j + 1, n -1
                while l < r:
                    #present sum of quardapule
                    total = nums[i] + nums[j] + nums[l] + nums[r]

                    if total == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])

                        #Checking those conditions
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1

                        while l < r and nums[r] == nums[r -1]:
                            r -= 1

                        l += 1
                        r -= 1

                    elif total < target:
                        l += 1
                    else:
                        r -= 1


        return res

# Example usage:
nums = [1, 0, -1, 0, -2, 2]
target = 0
solution = Solution()
result = solution.fourSum(nums, target)
print(result)
