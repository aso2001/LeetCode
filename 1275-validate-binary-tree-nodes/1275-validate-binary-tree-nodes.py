class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        def find_root():
            child = set(leftChild) | set(rightChild)
            for i in range(n):
                if i not in child:
                    return i 
            return -1
        
        root = find_root()
        if root == -1:
            return False
        
        seen = {root}
        stack = [root]
        while stack:
            node = stack.pop()
            for child in [leftChild[node], rightChild[node]]:
                if child != -1:
                    if child in seen:
                        return False
                    
                    stack.append(child)
                    seen.add(child)
        
        return len(seen) == n

        # dd = {}

        # for i in range(len(leftChild)):
        #     if leftChild[i] in dd: return False
        #     if leftChild[i] > 0: dd[leftChild[i]] = i
        #     if rightChild[i] in dd: return False
        #     if rightChild[i] > 0: dd[rightChild[i]] = i
        # print(dd)
        # if len(leftChild) == 2 and len(dd) < len(leftChild):
        #     return False
        # return True