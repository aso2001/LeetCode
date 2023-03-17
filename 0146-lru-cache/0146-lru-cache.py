class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
            
class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0 

    def add_to_head(self, node):
        node.next = self.head
        node.prev = None
        if self.head:
            self.head.prev = node
        self.head = node
        if not self.tail:
            self.tail = self.head
        self.size += 1

    def remove_node(self, node):
        if not node:
            return
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if self.head is node:
            self.head = node.next
        if self.tail is node:
            self.tail = node.prev
        self.size -= 1

    def print_dll(self):
        node = self.head
        while node:
            print(node.data[0],"-> ",end="")
            node = node.next
        print("")

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.DLL = DLL()
        self.dict = {}
        
    def get(self, key: int) -> int:
        if key in self.dict:
            node_tbm = self.dict[key]
            self.DLL.remove_node(node_tbm)
            self.DLL.add_to_head(node_tbm)
            return node_tbm.data[1]
        else: return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.dict:
            if self.DLL.size >= self.capacity:
                del self.dict[self.DLL.tail.data[0]]
                self.DLL.remove_node(self.DLL.tail)
            new_node = Node([key,value])
            self.DLL.add_to_head(new_node)
            self.dict[key] = new_node
        else:
            node_tbum = self.dict[key]
            node_tbum.data[1] = value
            self.DLL.remove_node(node_tbum)
            self.DLL.add_to_head(node_tbum)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)