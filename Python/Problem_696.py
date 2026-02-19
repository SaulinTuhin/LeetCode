# Problem - 696. Count Binary Substrings
# Python3 Solution!
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev_len = 0
        cur_len = 1
        res = 0
        
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                cur_len += 1
            else:
                res += min(prev_len, cur_len)
                prev_len = cur_len
                cur_len = 1
        
        return res + min(prev_len, cur_len)


if __name__=='__main__':
    sol = Solution()
    
    print(sol.countBinarySubstrings('00110011'))
    print(sol.countBinarySubstrings('10101'))