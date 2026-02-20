# Problem - 761. Special Binary String
# Python3 Solution!
class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = 0
        start = 0
        res = []
        
        for end, char in enumerate(s):
            if char == '1': count += 1
            else: count -= 1
            
            if count == 0:
                res.append('1' + self.makeLargestSpecial(s[start+1:end]) + '0')
                start = end + 1
                
        res.sort(reverse=True)
        return "".join(res)


if __name__=="__main__":
    sol = Solution()
    
    print(sol.makeLargestSpecial("11011000"))
    print(sol.makeLargestSpecial("10"))