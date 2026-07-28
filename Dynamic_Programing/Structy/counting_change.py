
'''
counting change

Write a function, counting_change, that takes in an amount and a list of coins. The function should return the number of different ways it is possible to make change for the given amount using the coins.

You may reuse a coin as many times as necessary.

For example,

counting_change(4, [1,2,3]) -> 4

There are four different ways to make an amount of 4:

1. 1 + 1 + 1 + 1
2. 1 + 1 + 2
3. 1 + 3
4. 2 + 2

counting_change(4, [1, 2, 3]) # -> 4

counting_change(8, [1, 2, 3]) # -> 10

counting_change(24, [5, 7, 3]) # -> 5

counting_change(13, [2, 6, 12, 10]) # -> 0

counting_change(512, [1, 5, 10, 25]) # -> 20119

counting_change(1000, [1, 5, 10, 25]) # -> 142511

counting_change(240, [1, 2, 3, 4, 5, 6, 7, 8, 9]) # -> 1525987916

'''

def counting_change(amount, coins):
  return _counting_change(amount, coins, 0, {})
  

# Here index represent for coins, you are choosing for.

def _counting_change(amount, coins, i, memo):
  key = (amount, i)

  #if key in the memo, return store value
  if key in memo:
    return memo[key]
  
  #Base case (how many ways to make 0 cents 
  #Do nothing , that means return 0
  if amount == 0:
    return 1

  if i == len(coins):
    return 0

  #Assign coin as a single value of coins[i]
  coin = coins[i]
  total_ways = 0
  
  for qty in range(0, (amount // coin) + 1):
    remainder = amount - (qty * coin)
    #Call recursively for the next index
    total_ways += _counting_change(remainder, coins, i + 1, memo)

  memo[key] = total_ways
  return total_ways
    
 
#   OR if you prefer individual test cases
 
if __name__ == "__main__":
    print(counting_change(4, [1, 2, 3]))                          # Expected: 4
    print(counting_change(8, [1, 2, 3]))                          # Expected: 10
    print(counting_change(24, [5, 7, 3]))                         # Expected: 5
    print(counting_change(13, [2, 6, 12, 10]))                    # Expected: 0
    print(counting_change(512, [1, 5, 10, 25]))                   # Expected: 20119
    print(counting_change(1000, [1, 5, 10, 25]))                  # Expected: 142511
    print(counting_change(240, [1, 2, 3, 4, 5, 6, 7, 8, 9]))      # Expected: 1525987916
