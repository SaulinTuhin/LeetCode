from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        ret = ''
        for s in strs:
            ret += str(len(s)) + '#' + s
        return ret

    def decode_0(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            length = ''
            while s[j] != '#':
                length += s[j]
                j += 1
            length = int(length)
            i = j + 1

            word = ''
            while length:
                word += s[i]
                length -= 1
                i += 1

            res.append(word)
        return res
    
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j +1 : j + 1 + length])
            i = j + 1 + length
        return res
    

if __name__=="__main__":
    sol = Solution()

    encode_out = sol.encode(["Hello","World"])
    print(encode_out)
    decode_out = sol.decode_0(encode_out)
    print(decode_out)