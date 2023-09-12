class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = Counter(s)
        deletions = 0
        used_freq= set()
        
        for char, freq in cnt.items():
            while freq > 0 and freq in used_freq:
                freq -= 1
                deletions += 1
            used_freq.add(freq)
            
        return deletions    