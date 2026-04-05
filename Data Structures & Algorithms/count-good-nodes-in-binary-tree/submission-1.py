# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.currMax = float('-inf')
        self.goodNodes = 0

        def dfs(node, currentMax):
            if not node:
                return
            # print (currentMax)
            if node.val>=currentMax:
                print (currentMax, node.val)

                self.goodNodes+=1
                currentMax = node.val
            dfs(node.left, currentMax)
            dfs(node.right, currentMax)
            
        dfs(root, root.val)
        return self.goodNodes