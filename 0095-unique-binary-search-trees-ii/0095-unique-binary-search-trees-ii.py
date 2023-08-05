# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        dp = [[[] for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][i] = [TreeNode(i)]

        for NoN in range(2, n + 1):
            for start in range(1, n - NoN + 2):
                end = start + NoN - 1
                for i in range(start, end + 1):
                    L_subtrees = dp[start][i - 1] if i != start else [None]
                    R_subtrees = dp[i + 1][end] if i != end else [None]

                    for L in L_subtrees:
                        for R in R_subtrees:
                            root = TreeNode(i, L, R)
                            dp[start][end].append(root)

        return dp[1][n]