
def howSum(targerSum, numbers,memo={}):

    if targerSum in memo:
        return memo[targerSum]
    #Base case
    if targerSum == 0:
        return []
    
    if targerSum < 0:
        return None
    
    #Recursive case
    for num in numbers:
        remainder = targerSum -num
        remainderResult = howSum(remainder, numbers, memo)

        if remainderResult is not  None:
            #Copy the whole remainderResult like this (...remainderResult)
            #store in the memo
            memo[targerSum] = [*remainderResult, num]
            return memo[targerSum]

        
    memo[targerSum] = None
    return None

#(for dp)->Time:O(n*m^2), Space:O(m^2); m = targerSum, n= array length

target = 7
nums = [2, 3]
result = howSum(target, nums)
print(f"Numbers that sum up to {target}: {result}")

#Output: Numbers that sum up to 7: [3,2, 2]
#NB: need to look back alvin's complexity explaiantion of this program