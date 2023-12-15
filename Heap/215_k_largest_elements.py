
#from collections 
import heapq

def findKthLargest(nums, k):
        #use a minheap to maintain the k largest elements
        heap = []

        #push the first kth element into the loop
        for num in nums[:k]:
            heapq.heappush(heap, num)
            #Modify the heap property as minheap
            heapq.heapify(heap)


        #For the remaining elements only push
        #them if this are larger than the smallest elements
        #in the heap
        for num in nums[k:]:
            if num > heap[0]:
                #then element remove from top of the heap
                heapq.heappop(heap)
                #then add element in the heap
                heapq.heappush(heap, num)
        
        #Finally , return the top of the heap which is kth largest element
        return heap[0]

nums = [3, 2, 1, 5, 4, 6]
k = 2
result = findKthLargest(nums, k)
print(result)