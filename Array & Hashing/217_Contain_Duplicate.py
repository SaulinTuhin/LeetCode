from typing import List

class Solution:
    def containsDuplicate_0(self, nums: List[int]) -> bool:
        """
        This is the sensible solution for coding interviews.
        O(n) -> Time & Space Complexity
        """
        seen = set()

        for n in nums:
            if n in seen:
                return True
        
        return False
    
    """
    Same thing, but python 🤓
    O(n) -> Time & Space
    """
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))
    
if __name__ == "__main__":
    sol  = Solution()

    print(sol.containsDuplicate([1,2,3,1]))
    print(sol.containsDuplicate([1,2,3,4]))
    print(sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))