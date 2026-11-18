"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque
from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        new = {node: Node(node.val)} # dict node : neighbors
        q = deque([node])
        while q:
            curr = q.popleft()
            for n in curr.neighbors: # iterate thru neighbors n
                if n not in new: # new node
                    new[n] = Node(n.val) # initialise to dict new
                    q.append(n)
                new[curr].neighbors.append(new[n]) # add n to neighbors of curr
        return new[node]
