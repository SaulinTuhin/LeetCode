# Problem - 1704: https://leetcode.com/problems/determine-if-string-halves-are-alike/
# Python3 Solution!
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        firstCount, secondCount = 0, 0

        i, j = 0, len(s)//2
        while i < len(s)/2:
            if s[i] in 'aeiouAEIOU':
                firstCount += 1
            if s[j] in 'aeiouAEIOU':
                secondCount += 1
            i += 1
            j += 1

        return firstCount == secondCount


if __name__=="__main__":
    sol = Solution()

    print(sol.halvesAreAlike("book"))
    print(sol.halvesAreAlike("textbook"))

