import collections


# https://leetcode.com/problems/number-of-recent-calls/description/
class RecentCounter:
    def __init__(self):
        self.requests = collections.deque()

    def ping(self, t: int) -> int:
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()
        self.requests.append(t)
        return len(self.requests)


# https://leetcode.com/problems/moving-average-from-data-stream/description/
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.sum = 0
        self.queue = collections.deque()

    def next(self, val: int) -> float:
        self.queue.append(val)
        first = self.queue.popleft() if len(self.queue) > self.size else 0
        self.sum += val - first
        return self.sum / len(self.queue)


if __name__ == "__main__":
    counter = RecentCounter()
    print(counter.ping(1))
    print(counter.ping(100))
    print(counter.ping(3001))
    print(counter.ping(3002))

    moving = MovingAverage(3)
    print(moving.next(1))
    print(moving.next(10))
    print(moving.next(3))
    print(moving.next(5))
