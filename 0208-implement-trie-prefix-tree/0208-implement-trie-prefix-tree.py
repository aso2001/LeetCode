class TrieNode:
    def __init__(self):
        self.child = [None]*26
        self.isLast = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not cur.child[idx]:
                cur.child[idx] = TrieNode()
            cur = cur.child[idx]
        cur.isLast = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not cur.child[idx]:
                return False
            cur = cur.child[idx]
        return cur.isLast
        
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            idx = ord(c) - ord('a')
            if not cur.child[idx]:
                return False
            cur = cur.child[idx]
        return True
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)