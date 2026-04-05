# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        
        def sameTree(node, subnode):
            if not node and not subnode:
                return True
            if not node or not subnode:
                return False

            if node.val!=subnode.val:
                return False
            
            left = sameTree(node.left, subnode.left)
            right = sameTree(node.right, subnode.right)


            return left and right
        
        def isSubTree(node, subnode):
            if not node and not subnode:
                return True
            if not node:
                return False
            if sameTree(node, subnode):
                return True
            
            left = isSubTree(node.left, subnode)
            right = isSubTree(node.right, subnode)

            return left or right
        
        return isSubTree(root, subRoot)

            
