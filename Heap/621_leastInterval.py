from collections import Counter
import heapq
'''
---Leet code 621:Task Scheduler:
  Given, a characters array tasks, representing the tasks a 
  CPU needs to do, where each letter represents a different
  task. Tasks could be done in any order.Each task is done one unit 
  of time. For each unit of time, the CPU could complete either 
  one task or just be idle.

   However, there is a non-negative integer n that represents
   the cooldown perid between two same tasks(the same letter in the 
   array), that is that there must be at least n units of time between
   any two same tasks.

   Return the least number of units of times that the CPU will take
   to finish all the given tasks.

   Example 1:

   Input: tasks = ["A", "A", "A", "B", "B", "B"], n = 2
   Explanation: A-> B-> idle -> A -> B -> idle -> A -> B
   There is at least 2 units of time between any two same tasks
   

'''


def leastInterval(tasks, n):
    
    #Creates a Counter object freq that counts the frequency
    #of each task in the input list tasks
    freq = Counter(tasks)

    #Create heap with negative frequencies of tasks.Negative values are used
    #because Pyhton's "heapq" library creates a min-heap, we want to protize
    #tasks with higher frequencies(That means build max-heap)
    heap = [-f for f in freq.values()]

    #Convert the list "heap" into a heap data structure through heap properties
    heapq.heapify(heap)

    #Initializes the variable times to the count numtes of interval needed
    times = 0


    #Enter the loop that continues untill the heap is empty(all tasks are scheduled)
    while heap:
        #Initializes am empty list to represent the cooldown period or interval period
        cooldown = []

        #loops n + 1 times to the cooldown period
        for i in range(n + 1):
            #Cehcks if the heap is not empty before popping elements.
            if heap:
                #Pops an element from the heap(negative freqeuncy) and 
                #adds 1 to simulate task execution. This represents
                #scheduling a task and its cooldown period
                cooldown.append(heapq.heappop(heap) + 1)
        
        #Iterate through the cooldown period
        for item in cooldown:

            #Checks if the item represents a task(negative value)
            if item < 0:
                #Then adds the tasks back to the heap for furhter scheduling
                heap.append(item)
        
        #Checks if there is remaining tasks in the heap
        if heap:
            #If there are remaining tasks, adds the length of the 
            #cooldown period plus tasks executed
            times += n + 1
        else:
            #If the heap is empty(no remaining tasks), adds the length
            #of the remaining cooldown period
            times += len(cooldown)
        
        #Rebuilds the heap for the next round of scheduling
        heapq.heapify(heap)
    
    #Finally, returns the total number of heap for the next round of
    #scheduling
    return times

tasks = ["A", "A", "A", "B", "B", "B"]
cooldown = 2
result = leastInterval(tasks, cooldown)
print(result) # Output will be the minimum number of intervals needed (8)
#This code uses a heap to priotize the tasks with the most freqeuncy and 
#schedules them according to meet the cooldown requirements
