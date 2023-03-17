class Solution:
    def rotate(self, mx: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(mx)-1):
            for j in range(i, len(mx)):
                mx[i][j], mx[j][i] = mx[j][i], mx[i][j]
        
        for i in range(len(mx)):
            for j in range(len(mx)//2):
                mx[i][j], mx[i][len(mx)-1-j] = mx[i][len(mx)-1-j], mx[i][j]

        # (a,b) => (b,L-a)
        #      |||
        # (a,b) => (b,a)
        # (b,a) => (b,L-a)

        # 5  1  9  11     5  2  13 15     15 13 2 5
        # 2  4  8  10     1  4  3  14     14 3  4 1
        # 13 3  6  7      9  8  6  12     12 6  8 9
        # 15 14 12 16     11 10 7  16     16 7 10 11

        #         \                   |
        #           \                 |
        #             \               |
        #               \             |