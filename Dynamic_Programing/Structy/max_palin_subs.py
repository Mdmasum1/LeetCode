'''
max palin subsequence

Write a function, max_palin_subsequence, that takes in a string as an argument. The function should return the length of the longest subsequence of the string that is also a palindrome.

A subsequence of a string can be created by deleting any characters of the string, while maintaining the relative order of characters.

max_palin_subsequence("luwxult") # -> 5

max_palin_subsequence("xyzaxxzy") # -> 6

max_palin_subsequence("lol") # -> 3

max_palin_subsequence("boabcdefop") # -> 3

max_palin_subsequence("z") # -> 1

max_palin_subsequence("chartreusepugvicefree") # -> 7

max_palin_subsequence("qwueoiuahsdjnweuueueunasdnmnqweuzqwerty") # -> 15

max_palin_subsequence("enamelpinportlandtildecoldpressedironyflannelsemioticsedisonbulbfashion

'''


def max_palin_subsequence(string):
  return _max_palin_subsequence(string, 0, len(string) - 1, {})
  


def _max_palin_subsequence(string, i , j, memo):

  key = (i, j)
  if key in memo:
    return memo[key]
    
  #base case 
  if i == j:
     return 1

  if i > j:
    return 0

  #Recursive case
  if string[i] == string[j]:
    memo[key] = 2 + _max_palin_subsequence(string, i + 1, j -1, memo)

  else:
    memo[key] = max(
      _max_palin_subsequence(string, i + 1, j, memo),
      _max_palin_subsequence(string, i, j - 1, memo)
      
    )

  return memo[key]
    
#Test cases
if __name__ == "__main__":
    print(f"max_palin_subsequence('bb') = {max_palin_subsequence('bb')}")
    print(f"max_palin_subsequence('bbbab') = {max_palin_subsequence('bbbab')}")
    print(f"max_palin_subsequence('cbbd') = {max_palin_subsequence('cbbd')}")
    print(f"max_palin_subsequence('a') = {max_palin_subsequence('a')}")
    print(f"max_palin_subsequence('') = {max_palin_subsequence('')}")
    print(f"max_palin_subsequence('abcde') = {max_palin_subsequence('abcde')}")
    print(f"max_palin_subsequence('agbdba') = {max_palin_subsequence('agbdba')}")
    print(f"max_palin_subsequence('character') = {max_palin_subsequence('character')}")