"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    # DFS recursively
    def cloneGraph2(self, node: 'Node') -> 'Node':

        dd = {} # map of [oldNode] -> newNode

        def dfs(node):
            if not node:
                return None

            if node in dd:
                return dd[node]

            dd[node] = Node(node.val)

            for nei in node.neighbors:
                dd[node].neighbors.append(dfs(nei))
            return dd[node]

        return dfs(node)

    
    # DFS iteratively
    def cloneGraph3(self, node: 'Node') -> 'Node':
        if not node:
            return node

        dd = {node: Node(node.val)}
        stack = [node]

        while stack:
            cur = stack.pop()
            for nei in cur.neighbors:
                if nei not in dd:
                    dd[nei] = Node(nei.val)
                    stack.append(nei)
                dd[cur].neighbors.append(dd[nei])
        return dd[node]

    
    # BFS iteratively
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
            
        dd = {node: Node(node.val)}
        q = collections.deque([node])

        while q:
            cur = q.popleft()
            for nei in cur.neighbors:
                if nei not in dd:
                    dd[nei] = Node(nei.val)
                    q.append(nei)
                dd[cur].neighbors.append(dd[nei])
        return dd[node]