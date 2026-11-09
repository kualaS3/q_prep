from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        result = []
        queue = deque([root])
        while queue:
            lvl_size = len(queue)
            lvl = []
            for _ in range(lvl_size):
                curr = queue.popleft()
                lvl.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result.append(lvl)
        return result
