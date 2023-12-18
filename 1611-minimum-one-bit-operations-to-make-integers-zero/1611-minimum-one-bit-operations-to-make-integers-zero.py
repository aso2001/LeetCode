class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        nbin = bin(n)
        sn = str(nbin[2:])
        st = []
        for i in range(len(sn) - 1, -1, -1):
            if sn[i] == '1':
                st.append(2**(len(sn) - i) - 1)
        res = 0
        for i in range(len(st)):
            res = st[i] - res
        return res