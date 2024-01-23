class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def valid(dd):
            if not len(dd):
                return False
            for d in dd:
                if dd[d] > 1:
                    return False
            return True

        def add_cnd(i, dd):
            for c in arr[i]:
                if c in dd:
                    dd[c] += 1
                else:
                    dd[c] = 1
        
        def rem_cnd(i, dd):
            for c in arr[i]:
                if dd[c] == 1:
                    del dd[c]
                else: 
                    dd[c] -= 1

        def backtrack(i, dd):
            nonlocal res
            if valid(dd):
                res = max(res, len(dd))

            for j in range(i + 1, len(arr)):
                add_cnd(j, dd)
                backtrack(j, dd)
                rem_cnd(j, dd)

        dd, res = {}, 0
        backtrack(-1, dd)
        return res