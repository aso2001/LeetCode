# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k == 0: return [target.val]
        dd = defaultdict(list)
        q = deque([root])
        while q:
            cur = q.popleft()
            if cur.left:
                if cur.val in dd:
                    dd[cur.val].append(cur.left.val)
                else:
                    dd[cur.val] = [cur.left.val]
                if cur.left.val in dd:
                    dd[cur.left.val].append(cur.val)
                else:
                    dd[cur.left.val] = [cur.val]
                q.append(cur.left)
            if cur.right:
                if cur.val in dd:
                    dd[cur.val].append(cur.right.val)
                else:
                    dd[cur.val] = [cur.right.val]
                if cur.right.val in dd:
                    dd[cur.right.val].append(cur.val)
                else:
                    dd[cur.right.val] = [cur.val]
                q.append(cur.right)
        
        nxt = deque()
        q = deque([target.val])
        visited = set()
        lev = 0
        while True:
            while q:
                cur = q.popleft()
                visited.add(cur)
                for nei in dd[cur]:
                    if nei not in visited:
                        nxt.append(nei)
            lev += 1
            if lev == k:
                return [*nxt]
            else:
                q = nxt.copy()
                nxt = deque()