
import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Use a minheap to maintain the k largest elements
        heap = []

        # Push the first kth element into the heap
        for num in nums[:k]:
            heapq.heappush(heap, num)

        # For the remaining elements, only push them if they are larger than the smallest elements in the heap
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

        # Finally, return the top of the heap which is the kth largest element
        return heap[0]

# Example input
nums = [3, 2, 1, 5, 6, 4]
k = 2

# Create an instance of the Solution class
sol = Solution()

# Calculate the kth largest element
result = sol.findKthLargest(nums, k)
print(f"The {k}th largest element is:", result)
