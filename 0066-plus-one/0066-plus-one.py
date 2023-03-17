class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        else:
            i = 0
            while i < len(digits) and digits[-1 - i] == 9:
                digits[-1 - i] = 0
                i += 1
            if i == len(digits):
                return [1] + digits
            else:
                digits[-1 - i] += 1
                return digits