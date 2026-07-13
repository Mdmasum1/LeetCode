'''
sum possible:

Write a function sum_possible that takes in an amount and a list of positive numbers. The function should return a boolean indicating whether or not it is possible to create the amount by summing numbers of the list. You may reuse numbers of the list as many times as necessary.

You may assume that the target amount is non-negative.

Example:
sum_possible(8, [5, 12, 4]) # -> True, 4 + 4

sum_possible(15, [6, 2, 10, 19]) # -> False

sum_possible(0, []) # -> True

#Complexity is T:O(a*n), s:O(a)


'''

def sum_possible(amount, numbers):
  return _sum_possible(amount, numbers, {})


def _sum_possible(amount, numbers, memo):

  #if you find amount in  memo as key then return memo add amount as a value
  if amount in memo:
    return memo[amount]
    

  #Corner cases; Checking for negetive numbers
  if amount < 0:
    return False
    
  if amount == 0:
    return True

  #Recursive case
  for num in numbers:
    #Pass this memo in the return call
    if _sum_possible(amount - num, numbers, memo) == True:
      memo[amount] = True
      return True

  #After for loop , you want return False
  memo[amount] = False
  return False
  


  
if __name__ == "__main__":
    tests = [
        (8, [5, 12, 4]),
        (15, [6, 2, 10, 19]),
        (0, []),
        (12, [2, 4]),
        (17, [2, 4]),
    ]
    for amount, numbers in tests:
        result = sum_possible(amount, numbers)
        print(f"sum_possible({amount}, {numbers}) = {result}")
 
'''
output:
sum_possible(8, [5, 12, 4]) = True
sum_possible(15, [6, 2, 10, 19]) = False
sum_possible(0, []) = True
sum_possible(12, [2, 4]) = True
sum_possible(17, [2, 4]) = False

'''