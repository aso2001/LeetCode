class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {_: 0 for _ in nums}
        mxcnt = 0
        for tmp in d:
            cnt = 1
            if d[tmp] == 1:
                continue
            if tmp - 1 not in d:   # tmp is the beginning of the sequence
                while tmp + 1 in d:
                    d[tmp + 1] = 1
                    tmp += 1
                    cnt += 1
            mxcnt = max(mxcnt, cnt)
        return mxcnt

    
    def longestConsecutive2(self, nums: List[int]) -> int:
        d = {_: 0 for _ in nums}
        mxcnt = 0
        for tmp in d:
            cnt = 1
            if d[tmp] == 1:
                continue
            prev = tmp
            while tmp + 1 in d and d[tmp + 1] != 1:
                d[tmp + 1] = 1
                tmp += 1
                cnt += 1
            tmp = prev
            while tmp - 1 in d and d[tmp - 1] != 1:
                d[tmp - 1] = 1
                tmp -= 1
                cnt += 1
            mxcnt = max(mxcnt, cnt)
        return mxcnt