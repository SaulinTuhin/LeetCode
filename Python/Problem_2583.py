from collections import deque
import heapq
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Problem - 2583. Kth Largest Sum in a Binary Tree
# Python3 Solution!
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = deque([root])
        min_heap = []
        
        while q:
            sum = 0
            for i in range(len(q)):
                cur = q.popleft()
                sum += cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            heapq.heappush(min_heap, sum)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return -1 if len(min_heap) < k else min_heap[0]
    

if __name__=="__main__":
    sol = Solution()
    
    def createTree(i, arr):
        if i >= len(arr) or not arr[i]:
            return None
        
        return TreeNode(arr[i], createTree(i*2 + 1, arr), createTree(i*2 + 2, arr))
    
    print(sol.kthLargestLevelSum(createTree(0, [5,8,9,2,1,3,7,4,6]), 2))
    print(sol.kthLargestLevelSum(createTree(0, [1,2,None,3]), 1))