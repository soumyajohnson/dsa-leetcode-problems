class Node:
    def __init__(self,key, val):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.cache={}
        self.head=Node(-1,-1)
        self.tail=Node(-1,-1)
        self.head.next=self.tail
        self.tail.prev=self.head


    def insert(self,node):
        last=self.tail.prev
        last.next=node
        node.prev=last
        node.next=self.tail
        self.tail.prev=node

    def remove(self, node):
        prev_node=node.prev
        next_node=node.next
        prev_node.next=next_node
        next_node.prev=prev_node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node=self.cache[key]
            node.val=value
            self.remove(node)
            self.insert(node)
        else:
            self.cache[key]=Node(key,value)
            self.insert(self.cache[key])
            if len(self.cache)>self.cap:
                lru=self.head.next
                self.remove(lru)
                del self.cache[lru.key]
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)