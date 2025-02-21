from collections import deque
from typing import Optional, Any


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


def range_sum_bst(root: TreeNode, low: int, high: int) -> int:
    if not root:
        return 0
    answer = 0
    if low <= root.val <= high:
        answer += root.val

    if low < root.val:
        answer += range_sum_bst(root.left, low, high)
    if high > root.val:
        answer += range_sum_bst(root.right, low, high)

    return answer


def range_sum_bst_iterative(root: TreeNode, low: int, high: int) -> int:
    stack = [root]
    answer = 0

    while stack:
        node = stack.pop()
        if low <= node.val <= high:
            answer += node.val
        if node.left and low < node.val:
            stack.append(node.left)
        if node.right and high > node.val:
            stack.append(node.right)
    return answer


def get_minimum_difference(root: TreeNode) -> int:
    def dfs(node: TreeNode):
        if not node:
            return
        dfs(node.left)
        values.append(node.val)  # inorder
        dfs(node.right)

        return node.val

    values = []
    dfs(root)
    answer = float("inf")
    for index in range(1, len(values)):
        answer = min(answer, values[index] - values[index - 1])
    return answer


def is_valid_bst(root: TreeNode) -> bool:
    def dfs(node: TreeNode, small: float, large: float) -> bool:
        if not node:
            return True

        if not (small < node.val < large):
            return False

        left = dfs(node.left, small, node.val)
        right = dfs(node.right, node.val, large)

        return left and right

    return dfs(root, float("-inf"), float("inf"))


def insert_into_bst(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return TreeNode(val)

    if val < root.val:
        if not root.left:
            root.left = TreeNode(val)
        insert_into_bst(root.left, val)
    if val > root.val:
        if not root.right:
            root.right = TreeNode(val)
        insert_into_bst(root.right, val)

    return root


class Solution:
    def __init__(self):
        self.answer = float("inf")
        self.difference = float("inf")

    def closest_value(self, root: Optional[TreeNode], target: float) -> int:
        def dfs(node, target):
            if not node:
                return float("inf")

            if self.difference > abs(target - node.val):
                self.difference = abs(target - node.val)
                self.answer = node.val
            if self.difference == abs(target - node.val):
                self.answer = min(self.answer, node.val)

            if target < node.val:
                dfs(node.left, target)
            else:
                dfs(node.right, target)
            return self.answer

        return dfs(root, target)


def print_tree(root: TreeNode) -> list[int]:
    result = []

    def dfs(node: TreeNode):
        if not node:
            return
        result.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return result


if __name__ == "__main__":
    # print(range_sum_bst(build_tree([10, 5, 15, 3, 7, None, 18]), 7, 15))
    # print(range_sum_bst_iterative(build_tree([10, 5, 15, 3, 7, None, 18]), 7, 15))
    # print(get_minimum_difference(build_tree([9, 5, 15, 1, 7])))
    # print(is_valid_bst(build_tree([10, 5, 12, 2, 8, None, 23])))
    # print(is_valid_bst(build_tree([40, 20, 60, 10, 30, 50, 70, None, None, 25])))
    # print(print_tree(insert_into_bst(build_tree([4, 2, 7, 1, 3]), 5)))
    # print(print_tree(insert_into_bst(build_tree([40, 20, 60, 10, 30, 50, 70, None, None, 25]), 25)))
    # print(Solution().closest_value(build_tree([4, 2, 5, 1, 3]), 3.714286))
    print(Solution().closest_value(build_tree([41,37,44,24,39,42,48,1,35,38,40,None,43,46,49,0,2,30,36,None,None,None,None,None,None,45,47,None,None,None,None,None,4,29,32,None,None,None,None,None,None,3,9,26,None,31,34,None,None,7,11,25,27,None,None,33,None,6,8,10,16,None,None,None,28,None,None,5,None,None,None,None,None,15,19,None,None,None,None,12,None,18,20,None,13,17,None,None,22,None,14,None,None,21,23]), 3.285714))
