
def howSum(targerSum, numbers):
    #Base case
    if targerSum == 0:
        return []
    
    if targerSum < 0:
        return None
    
    #Recursive case
    for num in numbers:
        remainder = targerSum -num
        remainderResult = howSum(remainder, numbers)

        if remainderResult is not  None:
            #Copy the whole remainderResult like this (...remainderResult)
            return [*remainderResult, num]
        
    
    return None
    
target = 7
nums = [2, 3]
result = howSum(target, nums)
print(f"Numbers that sum up to {target}: {result}")

#Output: Numbers that sum up to 7: [3,2, 2]