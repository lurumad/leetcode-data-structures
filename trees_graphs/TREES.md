# Trees

Like a linked list, a tree is a type of graph. Also like a linked list, there are multiple types of trees. In this course, we will be focusing on binary trees.

A binary tree is a collection of nodes. every node has between 0 and 2 children, and every node except the root has exactly one parent.

Trees (not just binary trees) are implemented all around us in a real life:

- File systems.
  - The root directory, and folders and subfolders.
- A comment thread on an app like X or Instagram.
  - The original post and the comments and replies.
- A company's organization chart.
  - The CEO and direct reports.

## Terminology

- Root
- Child
- Parent
- Leaf (No children, the leaves of the tree)
- Depth (How far a node is from the root node)
- Subtree

## Code representation

```python
class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
```



## DFS (Depth-First Search)

``the depth of a node is its distance from the root.``

In DFS, we prioritize depth by traversing as far down as possible in one direction (until reaching a lef node) before considering the other direction.

```python
def dfs(node):
    if node is None:
        return

    dfs(node.left)
    dfs(node.right)
    return
```

### Preorder traversal

The logic is done in the current node before moving their children.

```python
def preorder_dfs(node):
    if not node:
        return

    print(node.val)
    preorder_dfs(node.left)
    preorder_dfs(node.right)
    return
```

### Inorder traversal

First call the left child, the perform the logic on current node, and then recursively cal, the right child. 
No logic until we reach a node without a left child.
Left nodes will be handled until there are none, then the original node, then right nodes until there are none.

```python
def inorder_dfs(node):
    if not node:
        return

    inorder_dfs(node.left)
    print(node.val)
    inorder_dfs(node.right)
    return
```

### Postorder traversal

We recursively call on the children first and the n perform logic on the current node. No logic until we reach a leaf node.
Left nodes will be handled until there are none, then right nodes, then finally the original node.

```python
def postorder_dfs(node):
    if not node:
        return

    postorder_dfs(node.left)
    postorder_dfs(node.right)
    print(node.val)
    return
```

The name of each traversal is describing when the current node's logic is performed.

- Pre -> before children
- In -> in the middle of children
- Post -> after children

## BFS (Breadth-First Search)

In BSF, we prioritize breadth. traversing all the nodes at a given depth before moving on to the next depth.

BFS is implemented iteratively with a queue. You can implement BFS with recursion, but it wouldn't make sense as it's
a lot more difficult without any benefit.

## DFS vs DFS

### General Usage
- **DFS (Depth-First Search):**
  - Often used when the traversal order (preorder, inorder, postorder) does not matter as long as all nodes are visited.
  - Typically implemented using recursion, which results in simpler and more concise code.
  
- **BFS (Breadth-First Search):**
  - Best suited for problems requiring level-by-level processing of nodes.
  - Naturally handles scenarios where processing nodes according to their depth is necessary.

### When to Prefer BFS
- Use BFS when you need to process or analyze nodes according to their levels.
- Ideal for cases where the problem's requirements align with exploring the tree one level at a time.

### Drawbacks
- **DFS:**
  - May lead to inefficient searches if the target node is in a branch that is explored later. For example, if DFS prioritizes the left subtree and the target is in the right subtree, a significant portion of the tree might be unnecessarily traversed.

- **BFS:**
  - Can be time-inefficient when the target node is deep in the tree, as it must search through all preceding levels before reaching it.

### Space Complexity
- **DFS:**
  - Uses space proportional to the height (maximum depth) of the tree.
  - In a balanced binary tree, the space complexity is typically \( O(\log n) \).

- **BFS:**
  - Uses space proportional to the maximum number of nodes at any single level.
  - In a perfect binary tree, the last level might have \( O(n) \) nodes, leading to higher space requirements.
  - In contrast, in a lopsided tree (like a straight line), BFS might only need \( O(1) \) space.

### Conclusion
- **DFS** is generally preferred for its ease of implementation and lower code complexity when the order of traversal is not crucial.
- **BFS** is the better choice when level-order processing is required, despite its potential drawbacks in time and space usage depending on the tree's structure.

## Binary search trees

A Binary search tree is a type of binary tree but has the following property:

For each node, all the values in the left subtree are less than the value of the node, and all values in the right
subtree are greater tha the value of the node.

This also implies that values in BST must be unique.






