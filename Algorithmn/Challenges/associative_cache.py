# N Set-Way Associative Cache

def create_cache(n):
    cache = {}
    for i in range(1, n + 1, 1):
        cache[f'cache{i}'] = []
    return cache

print(create_cache(10))

class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev = None
        self.next = None

class LRUCache(object):
    def __init__(self, maxSize):
        self.cache = {}  # map key to node
        self.maxSize = maxSize or 1
    
    def insertKeyValue(self, key, value):
        if len(self.cache) >= self.maxSize:
            return "Error Cache Key exceeds"
        if key not in self.cache:
            self.cache[key] = value
        
    def getCache(self, key):
        if key in self.cache:
            return self.cache[key].value
        else:
            return -1