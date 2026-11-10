# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# a helper function is required to carry information down the recursion.
# needed memory of the parent when traversing to maintain tree integrity
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        return self.check(root, float('inf'), float('-inf'))
    
    def check(self, node, high, low):
        if node is None:
            return True
        if not low < node.val < high:
            return False
        return self.check(node.left, node.val, low) and self.check(node.right, high, node.val)
