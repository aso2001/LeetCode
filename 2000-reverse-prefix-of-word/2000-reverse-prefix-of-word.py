class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)
        if idx >= 0:
            word = word[:idx+1][::-1] + word[idx+1:]
        return word