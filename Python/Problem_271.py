from typing import List

# Problem - 271. Encode and Decode Strings
# Python3 Solution!
class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for w in strs:
            res += str(len(w)) + '#' + w
        return res
        
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i + 1
            while s[j] != '#':
                j += 1
            str_len = int(s[i:j])
            res.append(s[j + 1 : j + 1 + str_len])
            i = j + str_len + 1
        return res


if __name__=="__main__":
    sol = Solution()
    
    print(sol.decode(sol.encode(["neet","code","love","you"])) == ["neet","code","love","you"]) 
    print(sol.decode(sol.encode(["we","say",":","yes"])) == ["we","say",":","yes"]) 