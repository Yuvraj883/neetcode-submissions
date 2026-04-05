# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def dfs(node):
            if not node:
                return 0
            
            count1 = dfs(node.left)
            count2 = dfs(node.right)

            # return count1 if count1>count2 else count2
            return max(count1, count2)+1
        
        return dfs(root)
