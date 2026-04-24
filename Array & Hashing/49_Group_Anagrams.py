from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams_0(self, strs: List[str]) -> List[List[str]]:
        """
        Both are pretty much the same thing, with different hashing technique.
        I cannot think of any more brute force or efficient solution.
        O(n * k * log(k)) -> Time
        O(n * k) -> Memory
        """
        ang_dict = defaultdict(list[str])

        for s in strs:
            sorted_str = ''.join(sorted(s))
            ang_dict[sorted_str].append(s)
        
        return list(ang_dict.values())
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Will be faster if the size of individual strings (k) are very large.
        O(n * k) -> Time
        O(n * k) -> Memory
        """
        ang_dict = {}

        for s in strs:
            str_hash = [0] * 26
            for c in s:
                str_hash[ord(c) - ord('a')] += 1
            
            str_hash = tuple(str_hash)

            if str_hash not in ang_dict:
                ang_dict[str_hash] = []
            
            ang_dict[str_hash].append(s)
        
        return list(ang_dict.values())
    

if __name__=="__main__":
    sol = Solution()

    print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(sol.groupAnagrams([""]))
    print(sol.groupAnagrams(["a"]))