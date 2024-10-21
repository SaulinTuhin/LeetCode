# Problem - 1593. Split a String Into the Max Number of Unique Substrings
# Python3 Solution!
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        def dfs(i: int, hash_set: set) -> int:
            if i == len(s): return 0
            
            res = 0
            for j in range(i, len(s)):
                substr = s[i: j+1]
                if substr in hash_set:
                    continue
                
                hash_set.add(substr)
                res = max(res, 1 + dfs(j + 1, hash_set))
                hash_set.remove(substr)
            return res
        
        return dfs(0, set())
    
    
if __name__=="__main__":
    sol = Solution()
    
    print(sol.maxUniqueSplit("ababccc"))
    print(sol.maxUniqueSplit("aba"))
    print(sol.maxUniqueSplit("aa"))