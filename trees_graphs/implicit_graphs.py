from collections import deque
from typing import List


# https://leetcode.com/problems/open-the-lock/submissions/1563524967/
def open_lock(deadends: List[str], target: str) -> int:
    def neighbors(node):
        result = []
        for i in range(4):
            number = int(node[i])
            for change in [-1, 1]:
                x = (number + change) % 10
                result.append(node[:i] + str(x) + node[i + 1:])
        return result

    if "0000" in deadends:
        return -1

    queue = deque([("0000", 0)])
    seen = set(deadends)
    seen.add("0000")

    while queue:
        node, steps = queue.popleft()

        if node == target:
            return steps

        for neighbor in neighbors(node):
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append((neighbor, steps + 1))

    return -1


# https://leetcode.com/problems/evaluate-division/description/
def calc_equation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    pass


if __name__ == "__main__":
    print(open_lock(["0201", "0101", "0102", "1212", "2002"], "0202"))
