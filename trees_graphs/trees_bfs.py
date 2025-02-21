from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


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


def print_all_nodes(root: TreeNode):
    queue = deque([root])

    while queue:
        nodes_in_current_level = len(queue)

        for _ in range(nodes_in_current_level):
            node = queue.popleft()

            # do some logic here on the current node
            print(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


def binary_tree_right_side_view(root: TreeNode) -> list[int]:
    if not root:
        return []

    queue = deque([root])
    result = []

    while queue:
        nodes_in_current_level = len(queue)
        result.append(queue[-1].val)

        for _ in range(nodes_in_current_level):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result


def find_largest_value_each_row(root: TreeNode) -> list[int]:
    if not root:
        return []

    queue = deque([root])
    result = []

    while queue:
        maximum = float("-inf")
        nodes_in_current_level = len(queue)
        for _ in range(nodes_in_current_level):
            node = queue.popleft()
            maximum = max(maximum, node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(maximum)
    return result


def deepest_leaves_sum(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    queue = deque([root])
    result = 0

    while queue:
        nodes_in_current_level = len(queue)
        result = 0
        for _ in range(nodes_in_current_level):
            node = queue.popleft()
            if not node.left and not node.right:
                result += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result


def zigzag_level_order(root: TreeNode) -> list[list[int]]:
    if not root:
        return []

    queue = deque([root])
    result = []
    is_order_left = False
    while queue:
        level_list = deque()
        nodes_in_current_level = len(queue)
        for _ in range(nodes_in_current_level):
            node = queue.popleft()

            if is_order_left:
                level_list.appendleft(node.val)
            else:
                level_list.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(list(level_list))
        is_order_left = not is_order_left
    return result


if __name__ == "__main__":
    print(print_all_nodes(build_tree([1, 2, 3, 4, 5, 6])))
    print(binary_tree_right_side_view(build_tree([1, 2, 3, 4, 5])))
    print(find_largest_value_each_row(build_tree([1, 2, 9, 4, 5])))
    print(deepest_leaves_sum(build_tree([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8])))
    print(deepest_leaves_sum(build_tree([6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5])))
    print(zigzag_level_order(build_tree([3, 9, 20, None, None, 15, 7])))
    print(zigzag_level_order(build_tree([1])))
