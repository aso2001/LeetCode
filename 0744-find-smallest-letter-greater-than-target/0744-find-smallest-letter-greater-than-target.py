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


    def nextGreatestLetter2(self, letters: List[str], target: str) -> str:
        def binarySearch(t, L, R):

            while L <= R:
                mid = (L + R)//2
                if t < letters[mid]:
                    R = mid - 1
                elif t > letters[mid]:
                    L = mid + 1
                if L == R or L > R:
                    return letters[R]
                binarySearch(t, L, R)

        binarySearch(target, 0, len(letters) - 1)