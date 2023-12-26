
#P:Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

'''
---Intuition and plan for the problem step by step:
  ---Implementing k top frequency elements using a heap
  ---invloves using data structure like a max heap to efficiently
  ---find the elements with the highest freqeuncies in a given
  ---list or array.
   ---step by step:
    ---1. Traverse the list and count the frequencies of each elements
    ---2. use max or min heap to keep track of the k elements with highest frquencies
    ---3.Iterate throuhg the frequencies counts, adding elements to the 
         max heap until you have the k most frequent elements.


'''

from collections import Counter
import heapq

def topKFrequent(nums, k):
    #Count the frequency of each elments
    freq = Counter(nums)

    #Create a min heap
    heap = []

    #Iterate through the freqeuncy counts
    for num, frequency in freq.items():
        #Push element to the heap
        #While keeping only the top k elements with the highest frequencies
        heapq.heappush(heap, (frequency, num))
        
        #If heap length is greater that k then remove 
        #element from top of the heap
        if len(heap) > k:
            heapq.heappop(heap)

    #Extract the k most frequent elments from the heap into the answer
    answer = [element for frequency, element in heap]

    return answer



#Example:

nums1 = [1,1,1,2,2,3]

k = 2

result = topKFrequent(nums1, k)

print(f"The {k} most frequent elements are: {result}")


#Time: O(klogk) ; extracting the k most frequent elements from the
#heap
#Space:O(N)     ; Storing the frquency counts in the Cpunter
#and Oa9k) for maintaining the heap of k elements
