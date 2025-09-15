class Solution:
    def canBeTypedWords(self, text: str, broken: str) -> int:
        brokenKeys = set(broken)
        
        count = 0
        brokenWord = False
        n = len(text)
        for i in range(n + 1):
            if i < n and text[i] in brokenKeys:
                brokenWord = True
            if i == n or text[i] == ' ':
                if not brokenWord:
                    count += 1
                brokenWord = False
        return count