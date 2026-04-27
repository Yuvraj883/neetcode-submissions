# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        nodes = []
        def depthFirstSearch(node: TreeNode):
            if not node:
                return 
            
            depthFirstSearch(node.left)
            nodes.append(node.val)
            depthFirstSearch(node.right)

        depthFirstSearch(root)
        return nodes[k-1]

            
