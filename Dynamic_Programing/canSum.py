#Problem: Write a function 'canSum(targetSum, numbers)' that takes in a targetSum
# and an array of numbers as arguments

#The function should return a boolean indicating whether or not it is 
#possible to generate the targetSum using numbers form the array.

#You may use an element of the array as many times as needed. You may
# assume that all input numbers are nonnegative.

#Example: canSum(7, [5,3,4,7]) -> true;  here response will be 
#generate 7 to target 7.So should be True
#One way you could 3 + 4 = 7; another way 7 is target to 7
# But canSum(7, [2,4]) -> false

'''
# draw like tree data structure of this canSum()
-->    (7)
 -5 /-3|\   \-7
   /   | \   \
  (2) (4) (3) (0)
      / \   \-3
     (1) (0) (0)

#Here 2, 1, 0, are all those sorts out of base case.In this case , base case 0
#means they are back up to target sum. so those branch path sum only will be the
# target

NB:Keep in mind , this tree like data structure will implement
recursively as a brute force
--> Here , the question main point "is it possible at all to generate 
---the original target sum? So logic is when these boolean vlues return 
to their parent, the parent should just check if at least one of them is 
true. the parent should return true.

NB: exception or downside: some elment sort out to 1 base case , however that won't the 
element solution path

'''
def canSum(targetSum, numbers):
    # Base case: return True if targetSum is 0
    if targetSum == 0:
        return True
    #if target sum negative return false
    if targetSum < 0:
        return False

    # Recursive case: explore the recursive branch
    for num in range(len(numbers)):
        # Check if the current number is less than or equal to the targetSum
        if targetSum >= numbers[num]:
            # Subtract the current number from the targetSum and recursively check
            remainder = targetSum - numbers[num]
            #If this function generate from all remainder then return true
            if canSum(remainder, numbers) == True: # we use the numbers as parameter, 
                #because we use the array element as many as we want 
                return True

    # If no combination is found, return False(after the for loop)
    return False

var1 = print(canSum(7, [2, 3]))
var2 = print(canSum(7, [5, 3,4,7]))
var3 = print(canSum(7, [2, 4]))
var4 = print(canSum(7, [2, 3, 5]))
var5 = print(canSum(300, [7, 14]))
















