# Problem - 1957. Delete Characters to Make Fancy String
# Python3 Solution!
class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []    # Better memory
        # res = ''  # Better time
        prev_char = ''
        count = 0
        for char in s:
            if prev_char == char:
                if count == 2:
                    continue
                else:
                    count += 1
            else:
                count = 1
                prev_char = char
            res.append(char)
            # res += char
        return ''.join(res)
        # return res
    

if __name__=="__main__":
    sol = Solution()
    
    print(sol.makeFancyString("leeetcode"))
    print(sol.makeFancyString("aaabaaaa"))
    print(sol.makeFancyString("aab"))