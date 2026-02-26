class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
    
class DLL:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def removeFirst(self):
        if self.head.next==self.tail:
            return None
        node=self.head.next
        self.remove(node)
        return node
    
    def remove(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev
        node.prev=None
        node.next=None

    def addEnd(self,node):
        last=self.tail.prev
        last.next=node
        node.prev=last
        node.next=self.tail
        self.tail.prev=node

    def moveEnd(self,node):
        self.remove(node)
        self.addEnd(node)

class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.lrumap={}
        self.dll=DLL()

    def get(self, key: int) -> int:
        node=self.lrumap.get(key, None)
        if not node:
            return -1
        self.dll.moveEnd(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node=self.lrumap.get(key, None)
        if node:
            node.val=value
            self.dll.moveEnd(node)
        else:
            if len(self.lrumap)==self.cap:
                node=self.dll.removeFirst().key
                del self.lrumap[node]
            node=Node(key, value)
            self.dll.addEnd(node)
            self.lrumap[key]=node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)