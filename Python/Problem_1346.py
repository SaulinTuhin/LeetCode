from typing import List

# Problem - 1346. Check If N and Its Double Exist
# Python3 Solution!
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        visited = {arr[0]}
        for n in arr[1:]:
            if n * 2 in visited or (n % 2 == 0 and n // 2 in visited):
                return True
            visited.add(n)
        return False


if __name__=="__main__":
    sol = Solution()
    
    print(sol.checkIfExist([10,2,5,3]))
    print(sol.checkIfExist([3,1,7,11]))