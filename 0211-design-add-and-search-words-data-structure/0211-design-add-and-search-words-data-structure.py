class TrieNode:
    def __init__(self):
        self.child = {}
        self.isLast = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        self.max_length = 0

    def addWord(self, word: str) -> None:
        if len(word) > self.max_length:
            self.max_length = len(word)
        cur = self.root
        for c in word:
            if c not in cur.child:
                cur.child[c] = TrieNode()
            cur = cur.child[c]
        cur.isLast = True

    def search(self, word: str) -> bool:
        if len(word) > self.max_length:
            return False

        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for cc in cur.child.values():
                        if dfs(i + 1, cc):
                            return True
                    return False
                else:
                    if c not in cur.child:
                        return False
                    cur = cur.child[c]
            return cur.isLast
        
        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)