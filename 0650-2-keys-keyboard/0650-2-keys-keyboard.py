class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        self.n = n

        self.memo = [[0] * (n // 2 + 1) for _ in range(n + 1)]
        return 1 + self._min_steps_helper(1, 1)

    def _min_steps_helper(self, curr_len: int, paste_len: int) -> int:
        if curr_len == self.n:
            return 0
        if curr_len > self.n:
            return 1000
            
        if self.memo[curr_len][paste_len] != 0:
            return self.memo[curr_len][paste_len]

        opt1 = 1 + self._min_steps_helper(curr_len + paste_len, paste_len)
        opt2 = 2 + self._min_steps_helper(curr_len * 2, curr_len)
        self.memo[curr_len][paste_len] = min(opt1, opt2)
        return self.memo[curr_len][paste_len]