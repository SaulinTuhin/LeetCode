from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Problem - 1022. Sum of Root To Leaf Binary Numbers
# Python3 Solution!
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, cur_val):
            if not node:
                return 0
            
            cur_val = (cur_val << 1) | node.val

            if not node.left and not node.right:
                return cur_val
            
            return dfs(node.left, cur_val) + dfs(node.right, cur_val)
        
        return dfs(root, 0)


def to_binary_tree(items):
    if not items or items[0] is None:
        return None

    root = TreeNode(items[0])
    q = [root]
    i = 1
    for node in q:
        if i < len(items) and items[i] is not None:
            node.left = TreeNode(items[i])
            q.append(node.left)
        i += 1
        if i < len(items) and items[i] is not None:
            node.right = TreeNode(items[i])
            q.append(node.right)
        i += 1
    return root

if __name__=="__main__":
    sol = Solution()

    print(sol.sumRootToLeaf(to_binary_tree([1,0,1,0,1,0,1])))
    print(sol.sumRootToLeaf(to_binary_tree([0])))