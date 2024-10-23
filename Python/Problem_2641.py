from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Problem - 2641. Cousins in Binary Tree II
# Python3 Solution!
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level_sum = []
        q = deque([root])
        while q:
            cur_sum = 0
            for i in range(len(q)):
                node = q.popleft()
                cur_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level_sum.append(cur_sum)
            
        q = deque([(root, root.val)])
        level = 0
        while q:
            for i in range(len(q)):
                node, sibling_sum = q.popleft()
                node.val = level_sum[level] - sibling_sum
                
                child_sum = node.left.val if node.left else 0
                child_sum += node.right.val if node.right else 0
                if node.left:
                    q.append((node.left, child_sum))
                if node.right:
                    q.append((node.right, child_sum))
            level += 1
        return root


if __name__=="__main__":
    sol = Solution()
    
    def createTree(i, arr):
        if i >= len(arr) or not arr[i]:
            return None
        
        return TreeNode(arr[i], createTree(i * 2 + 1, arr), createTree(i * 2 + 2, arr))
    
    def printTree(root: TreeNode):
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                print(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        print('')
                
    printTree(sol.replaceValueInTree(createTree(0, [5,4,9,1,10,None,7])))
    printTree(sol.replaceValueInTree(createTree(0, [3,1,2])))