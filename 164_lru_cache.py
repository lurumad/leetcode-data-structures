from collections import OrderedDict


class LRUCache(OrderedDict):
    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self:
            self.move_to_end(key)
            return self[key]
        return -1

    def put(self, key: int, value: int) -> None:
        self[key] = value
        self.move_to_end(key)

        if len(self) > self.capacity:
            self.popitem(False)


if __name__ == "__main__":
    lru_cache = LRUCache(2)
    print(lru_cache.get(2))
    lru_cache.put(2, 6)
    print(lru_cache.get(1))
    lru_cache.put(1, 5)
    lru_cache.put(1, 2)
    print(lru_cache.get(1))
    print(lru_cache.get(2))
