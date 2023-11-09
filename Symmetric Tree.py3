# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirror(rootLeft, rootRight):
            if not rootLeft and not rootRight:
                return True
            elif not rootLeft or not rootRight:
                return False
            return rootLeft.val == rootRight.val and mirror(rootLeft.left, rootRight.right) and mirror(rootLeft.right, rootRight.left)
        return mirror(root, root)
            
