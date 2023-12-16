
def gridTraveler(m, n, memo={}):
    # Base case
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1
    

    #Create the key by string comma
    key = str(m) + ',' + str(n)
    
    # Checking if the arguments are in the memo
    if key in memo:
        return memo[key]
    
    # Recursive case
    memo[key] = gridTraveler(m - 1, n, memo) + gridTraveler(m, n - 1, memo)

    return memo[key]

result1 = gridTraveler(1, 1)
print(result1)
result2 = gridTraveler(2, 3)
print(result2)
result3 = gridTraveler(3, 2)
print(result3)
result4 = gridTraveler(3, 3)
print(result4)
result5 = gridTraveler(18, 18)
print(result5)
