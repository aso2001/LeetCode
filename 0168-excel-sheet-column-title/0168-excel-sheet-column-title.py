class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ''
        while columnNumber > 0:
            mod = (columnNumber - 1) % 26
            res += chr(mod + ord('A'))
            columnNumber = (columnNumber - 1) // 26      
        return res[::-1]