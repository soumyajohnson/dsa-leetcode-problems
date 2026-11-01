class Node:
    def __init__(self, key, value):
        self.value=value
        self.key=key
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.head=Node(-1,-1)
        self.tail=Node(-1,-1)
        self.head.next=self.tail
        self.tail.prev=self.head
    
    def insert_at_last(self, node:Node):
        latest=self.tail.prev
        latest.next=node
        node.prev=latest
        node.next=self.tail
        self.tail.prev=node

    def remove(self, node: Node):
        prev_node=node.prev
        next_node=node.next
        prev_node.next=next_node
        next_node.prev=prev_node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            value=self.cache[key].value
            self.remove(self.cache[key])
            self.insert_at_last(self.cache[key])
            return value


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value=value
            self.remove(self.cache[key])
            self.insert_at_last(self.cache[key])
        else:
            new_node=Node(key,value)
            self.cache[key]=new_node
            self.insert_at_last(new_node)
            if len(self.cache)>self.capacity:
                lru=self.head.next
                self.remove(lru)
                del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)