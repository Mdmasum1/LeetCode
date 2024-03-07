
import collections
from typing import List

'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]

'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use default dictionary to avoid typing error
        ans = collections.defaultdict(list)
        
        #looping through the group of the string
        for s in strs:

            #Initialize 0 with all 26 alphabets
            count = [0] * 26
            for c in s:
                #Increment the vlaue of the count
                count[ord(c) - ord("a")] += 1
            
            #Using tuple instead of list because tuple is immutable
            #and append s to the ans
            ans[tuple(count)].append(s)

        #Return the value of the dictionary
        return ans.values()

def main():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    solution = Solution()
    result = solution.groupAnagrams(strs)
    print(list(result))

if __name__ == "__main__":
    main()
