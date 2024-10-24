from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Problem - 951. Flip Equivalent Binary Trees
# Python3 Solution!
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 or not root2:
            return not root1 and not root2
        if root1.val != root2.val:
            return False

        chk_normal = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
        return chk_normal or (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))
        
if __name__=="__main__":
    sol = Solution()
    
    # TODO: Fix the makeTree function
    def makeTree(i, arr):   # Generates wrong tree for the 2nd input of first TC 😔
        if i >= len(arr) or not arr[i]:
            return None
        return TreeNode(arr[i], makeTree(i * 2 + 1, arr), makeTree(i * 2 + 2, arr))
    
    print(sol.flipEquiv(makeTree(0, [1,2,3,4,5,6,None,None,None,7,8]), 
                        makeTree(0, [1,3,2,None,6,4,5,None,None,None,None,8,7])))
    print(sol.flipEquiv(makeTree(0, []), makeTree(0, [])))
    print(sol.flipEquiv(makeTree(0, []), makeTree(0, [1])))