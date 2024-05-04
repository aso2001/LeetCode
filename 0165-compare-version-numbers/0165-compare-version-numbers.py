class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        sv1 = version1.split('.')
        sv2 = version2.split('.')
        length = max(len(sv1), len(sv2))

        for i in range(length):
            v1 = int(sv1[i]) if i < len(sv1) else 0
            v2 = int(sv2[i]) if i < len(sv2) else 0
            if v1 < v2:
                return -1
            if v1 > v2:
                return 1
        return 0