class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        def check(s, d):
            if len(s) < len(d):
                return False
            elif len(s) == len(d):
                return s == d
            else:
                if len(s)%len(d):
                    return False
                else:
                    i = 0
                    while i < len(s):
                        if s[i:i + len(d)] != d:
                            return False
                        i += len(d)
            return True

        lgcd = math.gcd(len(str1),len(str2))
        if str1[:lgcd] == str2[:lgcd] and check(str1, str1[:lgcd]) and check(str2, str2[:lgcd]):
            return str1[:lgcd]
        else:
            return ""