# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None:
            return False
        return (self.isSametree(root,subRoot)
                or self.isSubtree(root.left,subRoot)
                or self.isSubtree(root.right, subRoot))

    def isSametree(self, root, subRoot):
        if root is None or subRoot is None:
            return root is subRoot
        if root.val == subRoot.val:
            return self.isSametree(root.left, subRoot.left) and self.isSametree(root.right, subRoot.right)
        else:
            return False
