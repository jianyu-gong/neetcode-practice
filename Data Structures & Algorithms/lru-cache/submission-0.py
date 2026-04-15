class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.previous = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.previous = self.left

    def remove(self, node):
        pre = node.previous
        next = node.next

        pre.next = next
        next.previous = pre

    def insert(self, node):
        
        mru = self.right.previous

        mru.next = node
        node.next = self.right
        self.right.previous = node
        node.previous = mru

    def get(self, key: int) -> int:
        if key in self.cache:
            
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
