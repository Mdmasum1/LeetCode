#Leet code 125
'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 
'''
#Implement main  function 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
    
        while l < r:
            while l < r and not self.alphanum(s[l]):
                l += 1
            
            while l < r and not self.alphanum(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
        
            l += 1
            r -= 1
        
        return True
    
    def alphanum(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord('z')
            or ord("0") <= ord(c) <= ord('9')
        )

# Create an instance of the Solution class
solution = Solution()

# Test the isPalindrome function with an example string
s = "aba"
result = solution.isPalindrome(s)
print(result)
