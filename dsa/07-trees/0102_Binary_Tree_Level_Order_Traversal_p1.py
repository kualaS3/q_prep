# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:

        result = []

        def helper(root, level):
            if root is None: # node doesnt exist (is null)
                return None
            if level == len(result): # remb: level is updated by rec.
                result.append([])
            result[level].append(root.val)
            helper(root.left, level + 1)
            helper(root.right, level + 1)

        helper(root, 0) # this starts the loop, with the first node at lvl = 0

        return result
