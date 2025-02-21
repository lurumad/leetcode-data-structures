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


def playground_tree():
    root = built_tree()

    def dfs(node: TreeNode):
        if node is None:
            return

        print(node.val, end=' - ')
        dfs(node.left)
        dfs(node.right)

    dfs(root)


def built_tree():
    root = TreeNode(0)
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)
    six = TreeNode(6)
    root.left = one
    root.right = two
    one.left = three
    one.right = four
    four.right = six
    two.right = five
    return root


# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
def maximum_depth(root: TreeNode):
    def dfs(node: TreeNode, depth: int) -> int:
        if node is None:
            return depth
        depth_left = dfs(node.left, depth + 1)
        depth_right = dfs(node.right, depth + 1)

        return max(depth_left, depth_right)

    return dfs(root, 0)


def maximum_depth_stack(root: TreeNode) -> int:
    if not root:
        return 0

    stack = [(root, 1)]
    answer = 0

    while stack:
        node, depth = stack.pop()
        answer = max(answer, depth)
        if node.right:
            stack.append((node.right, depth + 1))
        if node.left:
            stack.append((node.left, depth + 1))

    return answer


# https://leetcode.com/problems/path-sum/submissions/1525334570/
def has_path_sum(root: TreeNode, target_sum: int) -> bool:
    if root is None:
        return False

    def dfs(node: TreeNode, current: int) -> bool:
        if node is None:
            return False

        if is_leaf_node(node):
            return node.val + current == target_sum

        left = dfs(node.left, node.val + current)
        right = dfs(node.right, node.val + current)

        return left or right

    def is_leaf_node(node):
        return node.left is None and node.right is None

    return dfs(root, 0)


def good_nodes(root: TreeNode):
    def dfs(node: TreeNode, previous: int) -> int:
        if node is None:
            return 0

        left = dfs(node.left, max(node.val, previous))
        right = dfs(node.right, max(node.val, previous))
        current = 1 if node.val >= previous else 0

        return left + right + current

    return dfs(root, 0)


# https://leetcode.com/problems/same-tree/
def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    if p is None and q is None:
        return True

    if p is None or q is None:
        return False

    return p.val == q.val and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode | None:
    if root is None:
        return None

    if root.val == p.val or root.val == q.val:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root

    return left if left else right


def minimum_depth(root: TreeNode) -> int:
    if root is None:
        return 0

    left = minimum_depth(root.left)
    right = minimum_depth(root.right)

    if left == 0:
        return right + 1

    if right == 0:
        return left + 1

    return 1 + min(left, right)


# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/
def max_difference(root: TreeNode) -> int:
    if not root:
        return 0

    def dfs(node: TreeNode, maximum: int, minimum: int) -> int:
        if not node:
            return maximum - minimum
        maximum = max(node.val, maximum)
        minimum = min(node.val, minimum)
        left = dfs(node.left, maximum, minimum)
        right = dfs(node.right, maximum, minimum)

        return max(left, right)

    return dfs(root, root.val, root.val)


class Solution:
    def __init__(self):
        self.result = 0

    def diameter_of_binary_tree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            self.result = max(self.result, left + right)
            return max(left, right) + 1

        dfs(root)
        return self.result


if __name__ == "__main__":
    # playground_tree()
    # print(maximum_depth(built_tree()))
    # print(maximum_depth_stack(built_tree()))
    # print(has_path_sum(built_tree(), 4))
    # print(good_nodes(build_tree([3, 1, 4, 3, None, 1, 5])))
    # print(good_nodes(build_tree([3, 3, None, 4, 2])))
    # print(good_nodes(build_tree([9, None, 3, 6])))
    # print(is_same_tree(build_tree([9, None, 3, 6]), build_tree([9, None, 3, 6])))
    # print(lowest_common_ancestor(build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]), TreeNode(5), TreeNode(4)).val)
    # print(minimum_depth(build_tree([3, 9, 20, None, None, 15, 7])))
    # print(minimum_depth(build_tree([2, None, 3, None, 4, None, 5, None, 6])))
    # print(max_difference(build_tree([8, 1, 2, 10, 11])))
    # print(max_difference(build_tree([1, None, 2, None, 0, 3])))
    print(Solution().diameter_of_binary_tree(build_tree([1, 2, 3, 4, 5])))
    print(Solution().diameter_of_binary_tree(build_tree(
        [4, -7, -3, None, None, -9, -3, 9, -7, -4, None, 6, None, -6, -6, None, None, 0, 6, 5, None, 9, None, None, -1,
         -4, None, None, None, -2])))
