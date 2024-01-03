'''
Sliding Window Technique:
  Definations: The sliding window technique involves creating a window
  of a fixed size or a size that moves through an array or string
to solve problems efficietly. It helps in reducing the time complexity 
by optimizing the brute-force approach.

Key Steps:

    1.Initialization: Define two pointers (usually, left and right) to represent the window's boundaries. Set them to the initial position.

    2.Iterate through the sequence: Move the right pointer to expand the window while meeting a certain condition.

    3.Optimize the window: Shrink the window by moving the left pointer when the condition is not met anymore, maintaining the window's optimal size.

    4.Update result/state: During or after window expansion/shrinkage, update the result or required data based on the problem statement.

    5.Repeat: Continue this process until the right pointer reaches the end of the sequence.

'''

#Problem: Find the maximum sum subarray of a fixed size k


def max_sum_subarray(arr, k):
    max_sum = float('-inf')
    window_sum = 0
    left = 0
    
    #Iterate through the input array
    for right in range(len(arr)):

        #Expand the window
        window_sum += arr[right]

        #Checking the condition to stop
        if right >= k -1:

            #update the result
            max_sum = max(max_sum, window_sum)

            #Contracting or shrinking the window by removing left pointer
            window_sum -= arr[left]
            
            #now left pointer moves to the right by incrementing
            left +=1

    #Return the result
    return max_sum

 
