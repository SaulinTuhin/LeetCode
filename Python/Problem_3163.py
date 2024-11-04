# Problem - 3163. String Compression III
# Python3 Solution!
class Solution:
    def compressedString(self, word: str) -> str:
        # comp = "" # uses less memory
        comp = []   # uses less time
        count = 1
        i = 1
        while i in range(1, len(word)):
            if word[i] == word[i - 1]:
                if count == 9:
                    # comp += '9' + word[i]
                    comp.append('9')
                    comp.append(word[i - 1])
                    count = 1
                else:
                    count += 1
            else:
                # comp += str(count) + word[i - 1]
                comp.append(str(count))
                comp.append(word[i - 1])
                count = 1
            i += 1
        # comp += str(count) + word[i - 1]
        comp.append(str(count))
        comp.append(word[i - 1])
        return ''.join(comp)


if __name__=="__main__":
    sol = Solution()
    
    print(sol.compressedString("abcde"))
    print(sol.compressedString("aaaaaaaaaaaaaabb"))
    print(sol.compressedString("d"))