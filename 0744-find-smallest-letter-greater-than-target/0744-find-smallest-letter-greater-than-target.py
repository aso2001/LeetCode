class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        L, R = 0, len(letters) - 1
        while L < R:
            mid = (L + R)//2
            if letters[mid] > target:
                R = mid
            else:
               L  = mid + 1
        return letters[R] if letters[R] > target else letters[0]