from collections import defaultdict, deque
from typing import List


# https://leetcode.com/problems/number-of-provinces/description/
def find_circle_num(is_connected: List[List[int]]) -> int:
    def dfs(node):
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                dfs(neighbor)

    # build the graph
    length = len(is_connected)
    graph = defaultdict(list)
    for i in range(length):
        for j in range(i + 1, length):
            if is_connected[i][j]:
                graph[i].append(j)
                graph[j].append(i)

    seen = set()
    answer = 0

    for i in range(length):
        if i not in seen:
            answer += 1
            seen.add(i)
            dfs(i)

    return answer


# https://leetcode.com/problems/number-of-islands/description/
def number_of_islands(grid: List[List[str]]) -> int:
    def valid(row, column):
        return 0 <= row < rows and 0 <= column < columns and grid[row][column] == "1"

    def dfs(row, column):
        for x, y in directions:
            next_row, next_column = row + x, column + y
            if (next_row, next_column) not in seen and valid(next_row, next_column):
                seen.add((next_row, next_column))
                dfs(next_row, next_column)

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    rows = len(grid)
    columns = len(grid[0])
    seen = set()
    answer = 0

    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == "1" and (row, column) not in seen:
                seen.add((row, column))
                answer += 1
                dfs(row, column)

    return answer


# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
def min_reorder(n: int, connections: List[List[int]]) -> int:
    roads = set()
    graph = defaultdict(list)
    for x, y in connections:
        graph[x].append(y)
        graph[y].append(x)
        roads.add((x, y))

    def dfs(node):
        answer = 0
        for neighbor in graph[node]:
            if neighbor not in seen:
                if (node, neighbor) in roads:
                    answer += 1
                seen.add(neighbor)
                answer += dfs(neighbor)
        return answer

    seen = {0}
    return dfs(0)


# https://leetcode.com/problems/keys-and-rooms/description/
def can_visit_all_rooms(rooms: List[List[int]]) -> bool:
    def dfs(node):
        for neighbor in rooms[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                dfs(neighbor)

    seen = {0}
    dfs(0)
    return len(rooms) == len(seen)


def find_smallest_set_of_vertices(n: int, edges: List[List[int]]) -> List[int]:
    indegrees = [0] * n

    for _, y in edges:
        indegrees[y] += 1

    return [node for node in range(n) if indegrees[node] == 0]


# https://leetcode.com/problems/find-if-path-exists-in-graph/editorial/
def valid_path_dfs(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    if source == destination:
        return True

    graph = defaultdict(list)
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    def dfs(node):
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                dfs(neighbor)

    seen = set()
    dfs(source)

    return destination in seen


# https://leetcode.com/problems/find-if-path-exists-in-graph/editorial/
# Time complexity: 0(n + m) n = nodes m = edges
# Space complexity: 0(n + m) n = nodes m = edges
def valid_path_bfs(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    if source == destination:
        return True

    graph = defaultdict(list)
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    seen = {source}
    queue = deque([source])

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor == destination:
                return True
            if neighbor not in seen:
                queue.append(neighbor)

    return False


# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/editorial/
def count_components(n: int, edges: List[List[int]]) -> int:
    graph = defaultdict(list)
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    def dfs(node):
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                dfs(neighbor)

    seen = set()
    answer = 0

    for i in range(n):
        if i not in seen:
            answer += 1
            dfs(i)

    return answer


# https://leetcode.com/problems/max-area-of-island/editorial/
def max_area_of_island(grid: List[List[int]]) -> int:
    def is_valid(row, column):
        return 0 <= row < rows and 0 <= column < columns and grid[row][column] == 1

    def dfs(row, column, size):
        for x, y in directions:
            next_row = row + y
            next_column = column + x
            if is_valid(next_row, next_column) and (next_row, next_column) not in seen:
                seen.add((next_row, next_column))
                size = dfs(next_row, next_column, size + 1)
        return size

    seen = set()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    rows = len(grid)
    columns = len(grid[0])
    max_size = 0

    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == 1 and (row, column) not in seen:
                seen.add((row, column))
                max_size = max(max_size, dfs(row, column, 1))

    return max_size


def max_area_of_island_iterative(grid: List[List[int]]) -> int:
    def is_valid(row, column):
        return 0 <= row < rows and 0 <= column < columns and grid[row][column] == 1

    def iterative(start_row, start_column) -> int:
        size = 1
        stack = [(start_row, start_column)]
        while stack:
            row, column = stack.pop()
            for x, y in directions:
                next_row = row + y
                next_column = column + x
                if is_valid(next_row, next_column) and (next_row, next_column) not in seen:
                    seen.add((next_row, next_column))
                    stack.append((next_row, next_column))
                    size += 1
        return size

    seen = set()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    rows = len(grid)
    columns = len(grid[0])
    max_size = 0

    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == 1 and (row, column) not in seen:
                seen.add((row, column))
                max_size = max(max_size, iterative(row, column))

    return max_size


def reachable_nodes(n: int, edges: List[List[int]], restricted: List[int]) -> int:
    graph = defaultdict(list)

    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    seen = set()
    seen.add(0)
    size = 1
    queue = deque([0])
    while queue:
        node = queue.popleft()
        if node in restricted:
            continue
        for neighbor in graph[node]:
            if neighbor not in seen and neighbor not in restricted:
                size += 1
                seen.add(neighbor)
                queue.append(neighbor)

    return size


if __name__ == "__main__":
    print(find_circle_num([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
    print(find_circle_num([[1, 0, 0], [1, 0, 0], [0, 0, 1]]))
    print(number_of_islands(
        [['1', "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]))
    print(min_reorder(6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]))
    print(can_visit_all_rooms([[1, 3], [3, 0, 1], [2], [0]]))
    print(find_smallest_set_of_vertices(6, [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]))
    print(valid_path_dfs(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5))
    print(valid_path_bfs(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 3, 5))
    print(count_components(5, [[0, 1], [1, 2], [3, 4]]))
    print(count_components(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))
    print(max_area_of_island([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                              [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                              [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))
    print(
        max_area_of_island_iterative([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                      [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                                      [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                                      [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                      [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))
    print(reachable_nodes(7, [[0, 1], [1, 2], [3, 1], [4, 0], [0, 5], [5, 6]], [4, 5]))
    # print(reachable_nodes(7, [[0, 1], {0, 2}, [0, 5], [0, 4], [3, 2], [6, 5]], [4, 2, 1]))
