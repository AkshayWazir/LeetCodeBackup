class LRUCache:

    def __init__(self, capacity: int):
        self.max_val = capacity
        self.keys = list()
        self.vals = dict()

    def get(self, key: int) -> int:
        res = self.vals.get(str(key), -1)
        if res != -1:
            self.keys.append(self.keys.pop(self.keys.index(str(key))))
        return res

    def put(self, key: int, value: int) -> None:
        try:
            self.keys.append(self.keys.pop(self.keys.index(str(key))))
            self.vals[str(key)] = value
        except ValueError:
            if len(self.keys) == self.max_val:
                self.vals.pop(self.keys.pop(0))
            self.vals[str(key)] = value
            self.keys.append(str(key))




# if len(self.keys) == self.max_val:
#     self.vals.pop(str(self.keys.pop(0)))
# self.vals[str(key)] = value
# if str(key) not in self.keys:
#     self.keys.append(str(key))


cache = LRUCache(2)
cache.put(2, 6)
print(cache.get(1))
cache.put(1, 5)
cache.put(1, 2)
print(cache.get(1))
print(cache.get(2))
