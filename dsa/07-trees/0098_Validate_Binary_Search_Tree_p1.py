# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        return self.check(root, float('inf'), float('-inf'))
    def check(self, root, high, low):
        if root is None:
            return True
        if root.val <= low or root.val >= high :
            return False
        return self.check(root.left, root.val, low) and self.check(root.right, high, root.val)
