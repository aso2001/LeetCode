class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x < y:
            s = s[::-1]
            x, y = y, x
        a_cnt, b_cnt, res = 0, 0, 0
        
        for i in range(len(s)):
            if s[i] == "a":
                a_cnt += 1
            elif s[i] == "b":
                if a_cnt > 0:
                    a_cnt -= 1
                    res += x
                else:
                    b_cnt += 1
            else:
                res += min(b_cnt, a_cnt) * y
                a_cnt = b_cnt = 0
        res += min(b_cnt, a_cnt) * y
        return res

    def maximumGain2(self, s: str, x: int, y: int) -> int:
        # TLE
        res = 0
        while s:
            if x >= y:
                p1 = s.find("ab")
                if p1 >= 0:
                    s = s[:p1] + s[p1+2:]
                    res += x
                else:
                    p2 = s.find("ba")
                    if p2 >= 0:
                        s = s[:p2] + s[p2+2:]
                        res += y
                    else:
                        return res
            else:
                p2 = s.find("ba")
                if p2 >= 0:
                    s = s[:p2] + s[p2+2:]
                    res += y
                else:
                    p1 = s.find("ab")
                    if p1 >= 0:
                        s = s[:p1] + s[p1+2:]
                        res += x
                    else:
                        return res
        return res