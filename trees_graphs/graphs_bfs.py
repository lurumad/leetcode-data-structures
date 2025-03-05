from collections import deque, defaultdict
from typing import List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


def build_tree(values):
    if not values:
        return None

    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()

    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()

    return root


# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/
def shortest_path_binary_matrix(grid: List[List[int]]) -> int:
    if grid[0][0] == 1:
        return -1

    def valid(row, column):
        return 0 <= row < length and 0 <= column < length and grid[row][column] == 0

    length = len(grid)
    seen = {(0, 0)}
    row, column, steps = 0, 0, 1
    queue = deque([(row, column, steps)])
    directions = [(0, 1), (1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1), (0, -1), (-1, 0)]

    while queue:
        row, column, steps = queue.popleft()

        if (row, column) == (length - 1, length - 1):
            return steps

        for dx, dy in directions:
            next_row = row + dy
            next_column = column + dx
            if valid(next_row, next_column) and (next_row, next_column) not in seen:
                seen.add((next_row, next_column))
                queue.append((next_row, next_column, steps + 1))

    return -1


# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/
def distance_k(root: TreeNode, target: TreeNode, k: int) -> List[int]:
    def dfs(node, parent):
        if not node:
            return
        node.parent = parent
        dfs(node.left, node)
        dfs(node.right, node)

    dfs(root, None)
    seen = {target}
    queue = deque([target])
    distance = 0

    while queue and distance < k:
        current_length = len(queue)
        for _ in range(current_length):
            node = queue.popleft()
            for neighbor in [node.left, node.right, node.parent]:
                if neighbor and neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        distance += 1

    return [node.val for node in queue]


# https://leetcode.com/problems/01-matrix/description/
def update_matrix(mat: List[List[int]]) -> List[List[int]]:
    def valid(row, column):
        return 0 <= row < rows and 0 <= column < columns

    rows = len(mat)
    columns = len(mat[0])
    queue = deque([])
    seen = set()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for row in range(rows):
        for column in range(columns):
            if mat[row][column] == 0:
                queue.append((row, column, 1))
                seen.add((row, column))

    while queue:
        row, column, step = queue.popleft()
        for dx, dy in directions:
            next_row = row + dy
            next_column = column + dx
            if valid(next_row, next_column) and (next_row, next_column) not in seen:
                seen.add((next_row, next_column))
                queue.append((next_row, next_column, step + 1))
                mat[next_row][next_column] = step

    return mat


def shortest_path(grid: List[List[int]], k: int) -> int:
    def valid(row, column):
        return 0 <= row < rows and 0 <= column < columns

    rows = len(grid)
    columns = len(grid[0])
    seen = {(0, 0, k)}
    row, column, steps = 0, 0, 0
    queue = deque([(row, column, k, steps)])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        row, column, k, steps = queue.popleft()

        if (row, column) == (rows - 1, columns - 1):
            return steps

        for dx, dy in directions:
            next_row = row + dy
            next_column = column + dx
            if valid(next_row, next_column) and (next_row, next_column, k) not in seen:
                if grid[next_row][next_column] == 1 and k > 0:
                    seen.add((next_row, next_column, k))
                    queue.append((next_row, next_column, k - 1, steps + 1))
                elif grid[next_row][next_column] == 0:
                    seen.add((next_row, next_column, k))
                    queue.append((next_row, next_column, k, steps + 1))

    return -1


# https://leetcode.com/problems/shortest-path-with-alternating-colors/
def shortest_alternating_paths(n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
    RED = 0
    BLUE = 1

    graph = defaultdict(lambda: defaultdict(list))
    for x, y in red_edges:
        graph[RED][x].append(y)
    for x, y in blue_edges:
        graph[BLUE][x].append(y)

    ans = [float("inf")] * n
    queue = deque([(0, RED, 0), (0, BLUE, 0)])
    seen = {(0, RED), (0, BLUE)}

    while queue:
        node, color, steps = queue.popleft()
        ans[node] = min(ans[node], steps)

        for neighbor in graph[color][node]:
            if (neighbor, 1 - color) not in seen:
                seen.add((neighbor, 1 - color))
                queue.append((neighbor, 1 - color, steps + 1))

    return [x if x != float("inf") else -1 for x in ans]


def nearest_exit(maze: List[List[str]], entrance: List[int]) -> int:
    def is_empty_cell(row, column):
        return 0 <= row < rows and 0 <= column < columns and maze[row][column] == "."

    def is_at_the_border(row, column):
        return row in [0, rows - 1] or column in [0, columns - 1]

    rows = len(maze)
    columns = len(maze[0])
    start_row, start_column = entrance
    maze[start_row][start_column] = "+"
    queue = deque([(start_row, start_column, 0)])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        row, column, steps = queue.popleft()

        for dx, dy in directions:
            next_row = row + dy
            next_column = column + dx
            if is_empty_cell(next_row, next_column):
                if is_at_the_border(next_row, next_column):
                    return steps + 1
                maze[next_row][next_column] = "+"
                queue.append((next_row, next_column, steps + 1))

    return -1


# [
# [-1,-1,-1,-1,-1,-1]
# [-1,-1,-1,-1,-1,-1]
# [-1,-1,-1,-1,-1,-1]
# [-1,35,-1,-1,13,-1]
# [-1,-1,-1,-1,-1,-1]
# [-1,15,-1,-1,-1,-1]
# ]
def snakes_and_ladders(board: List[List[int]]) -> int:
    rows = len(board)
    cells = [None] * (rows**2 + 1)
    label = 1
    columns = list(range(0, rows))
    for row in range(rows - 1, -1, -1):
        for column in columns:
            cells[label] = (row, column)
            label += 1
        columns.reverse()
    dist = [-1] * (rows * rows + 1)
    queue = deque([1])
    dist[1] = 0
    while queue:
        current = queue.popleft()
        for next in range(current + 1, min(current + 6, rows**2) + 1):
            row, column = cells[next]
            destination = (board[row][column] if board[row][column] != -1 else next)
            if dist[destination] == -1:
                dist[destination] = dist[current] + 1
                queue.append(destination)
    return dist[rows * rows]

    return -1


if __name__ == "__main__":
    # print(shortest_path_binary_matrix([[0, 1], [1, 0]]))
    # print(shortest_path_binary_matrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]]))
    # print(shortest_path_binary_matrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]))
    # print(update_matrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
    # print(shortest_path([[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]], 1))
    # print(shortest_path([[0, 1, 1], [1, 1, 1], [1, 0, 0]], 1))
    # print(shortest_alternating_paths(3, [[0, 1]], [[1, 2]]))
    # print(nearest_exit([["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]], [1, 2]))
    # print(nearest_exit([["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], [1, 0]))
    # print(nearest_exit([["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], [1, 0]))
    # print(nearest_exit([[".", "+"]], [0, 0]))
    # print(nearest_exit([[".", "."]], [0, 1]))
    print(snakes_and_ladders(
        [[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, 35, -1, -1, 13, -1],
         [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1]]))
