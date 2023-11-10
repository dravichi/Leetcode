# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        # Recursive
        def build(l, r):
            if l > r:
                return None
            mid = (l+r) // 2
            root = TreeNode(nums[mid])
            root.left = build(l, mid-1)
            root.right = build(mid+1, r)
            return root
        return build(0, len(nums)-1)

        # Iterative
        # if not nums:
        #     return None
        # root = TreeNode()
        # n = len(nums)
        # stack = [(root, 0, n-1)]
        # while stack:
        #     cur, left, right = stack.pop()
        #     mid = (left+right) // 2
        #     cur.val = nums[mid]
        #     if left <= mid - 1:
        #         cur.left = TreeNode()
        #         stack.append((cur.left, left, mid-1))
        #     if right >= mid + 1:
        #         cur.right = TreeNode()
        #         stack.append((cur.right, mid+1, right))
        # return root
