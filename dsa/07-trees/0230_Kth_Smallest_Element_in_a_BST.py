# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        count = 0
        ans = None
        # standard inorder DFS:
        # DFS(r.left), res.append(r.val), DFS(r.right)
        def DFS(root):
            # nonlocal makes them update the variables instead of create new local variables
            nonlocal count, ans 
            if root is None:
                return None
            DFS(root.left)
            count += 1
            if count == k :
                ans = root.val
            DFS(root.right)
        DFS(root)
        return ans
