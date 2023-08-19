import collections

# LRU Cache
# implementations via collections OrderedDict()
# cache.move_to_end(key) maintains the last recently access
# cache.popitem() pop the last recently access
# cache.popitem(last=False) pop the first item
class LRUCache:
    def __init__(self, capacity : int):
        self.cache = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: int):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1
        
    def put(self, key: int, value: int):
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            if self.capacity > 0:
                self.cache[key] = value
                self.cache.move_to_end(key)
                self.capacity -= 1
            else:
                self.cache.popitem(last=False)
                self.cache[key] = value
                self.cache.move_to_end(key)


cache = LRUCache(5)
cache.get(5)
cache.put(1,1)
cache.put(2,2)
cache.put(10,10)
cache.put(5,5)
cache.get(10)
cache.put(3,3)
cache.put(3,8)
cache.get(1)
print(cache.cache, cache.capacity)