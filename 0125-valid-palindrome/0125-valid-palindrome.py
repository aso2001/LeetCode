class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""
        s = s.lower()
        length = len(s)
        for i in range(length):
            if s[i].isalnum():
                newS += s[i]
        newS2 = newS[::-1]
        if newS == newS2:
            return True
        else:
            return False