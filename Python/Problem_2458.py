# Definition for a binary tree node.
from collections import deque
from functools import cache
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Problem - 2458. Height of Binary Tree After Subtree Removal Queries
# Python3 Solution!
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        
        @cache
        def get_height(node):
            if not node:
                return 0
            return max(get_height(node.left), get_height(node.right)) + 1
        
        lookup = {}
        def pre_calculate(node, depth, max_other):
            if not node:
                return
            
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            
            if node.left:
                lookup[node.left.val] = max(right_height + depth, max_other)
                pre_calculate(node.left, depth + 1, lookup[node.left.val])
            if node.right:
                lookup[node.right.val] = max(left_height + depth, max_other)
                pre_calculate(node.right, depth + 1, lookup[node.right.val])
                
        pre_calculate(root, 0, 0)
        
        res = []
        for q in queries:
            res.append(lookup[q])
        return res


if __name__=="__main__":
    sol = Solution()
    
    def createTree(arr):
        if not arr:
            return None
        it = iter(arr)
        root = TreeNode(next(it))
        q = [root]
        for node in q:
            cur = next(it, None)
            if cur:
                node.left = TreeNode(cur)
                q.append(node.left)
            cur = next(it, None)
            if cur:
                node.right = TreeNode(cur)
                q.append(node.right)
        return root
    
    print(sol.treeQueries(createTree([1,3,4,2,None,6,5,None,None,None,None,None,7]), [4]))
    print(sol.treeQueries(createTree([5,8,9,2,1,3,7,4,6]), [3,2,4,8]))