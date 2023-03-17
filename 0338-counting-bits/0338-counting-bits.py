class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(0,n+1):
            cnt = 0
            while i:
                cnt += i & 1
                i >>= 1
            res.append(cnt)
        return res
    
    
    def countBits2(self, n: int) -> List[int]:
        res = []
        for i in range(0,n+1):
            ib = str(bin(i))
            ib = ib[2:]
            cnt = 0
            for ii in range(0,len(ib)):
                if ib[ii] == '1':
                    cnt += 1
            res.append(cnt)
        return res