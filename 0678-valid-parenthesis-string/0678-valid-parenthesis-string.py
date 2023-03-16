class Solution:

    def checkValidString(self, s: str) -> bool:
        # Greedy O(n) 2 passes
        leftBalance = 0

        for c in s:
            if c == ')':
                leftBalance -= 1
            else:
                leftBalance += 1
            if leftBalance < 0:     # will eliminate ").." 
                return False
        if leftBalance == 0:
            return True

        rightBalance = 0
        for c in reversed(s):      
            if c == '(':
                rightBalance -= 1
            else:
                rightBalance += 1
            if rightBalance < 0:    # will eliminate in reversed "(*)("
                return False
        return True


    def checkValidString1(self, s: str) -> bool:
        # Greedy O(n)
        leftMin, leftMax = 0, 0
        for c in s:
            if c == '(':
                leftMin += 1
                leftMax += 1
            elif c == ')':
                leftMin -= 1
                leftMax -= 1
            else:
                leftMin -= 1
                leftMax += 1
            if leftMax < 0:
                return False
            if leftMin < 0: # s = (*)(
                leftMin = 0
        return leftMin == 0
    
    
    def checkValidString2(self, s: str) -> bool:
        # DP O(n^2)
        dp = {(len(s), 0): True} # key=(i, leftCount) -> isValid

        def dfs(i, left):
            if i == len(s) or left < 0:
                return left == 0
            if (i, left) in dp:
                return dp[(i, left)]
            if s[i] == '(':
                dp[(i, left)] = dfs(i + 1, left + 1)
            elif s[i] == ')':
                dp[(i, left)] = dfs(i + 1, left - 1)
            else:
                dp[(i, left)] = (dfs(i + 1, left + 1) or dfs(i + 1, left - 1) or dfs(i + 1, left))
            return dp[(i, left)]
        
        return dfs(0, 0)