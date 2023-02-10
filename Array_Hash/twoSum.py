'''
The Two Sum problem is a common problem in computer science that involves 
finding two integers in an array that sum to a specific target value. 
# Given an array of integers and a target value, the goal is to find two integers 
in the array that add up to the target value. For example, 
if the input array is [2, 7, 11, 15] and the target value is 9, 
the solution to the Two Sum problem would be the integers 2 and 7, since 2 + 7 = 9. 
The problem is often used to illustrate the concept of a hash table or a dictionary data structure.

'''
#I can use hashmap data structure to figure out the index
#which add up to target value


def twoSum(nums, target):
  # Create a dictionary to store the indices of the array elements
  map = {}
  for i, v in enumerate(nums):

    diff = target - v
    # If the target minus the current element exists in the dictionary, return the indices
    if diff in map:
      return [map[diff], i]
    # Otherwise, add the current element and its index to the dictionary
    # or you can say update the next index
    map[v] = i
  return []


#To call two sum function, you would simply call it
#like any other function, passing in the required
#arguments.
nums = [2, 7, 11, 15]
target = 9
result = twoSum(nums, target)
print(result)
