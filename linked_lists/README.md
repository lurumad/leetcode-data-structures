# Linked Lists

## What is a Linked List?

A linked list is a data structure that is similar to an array. It also stores data in an ordered manner, but it is implemented using node objects (you will have a custom class that defines the node object). Each node will have a "next" pointer, which points to the node representing the next element in the sequence.

## Advantages and Disadvantages of Linked Lists

### Advantages

- The main advantage of a linked list is that you can add and remove elements at any position in O(1).
- Resizing is cheaper than an array because you don't have to copy all the elements to a new array.

### Disadvantages

- The main disadvantage of a linked list is that you can't access elements by index. You have to start from the head and follow the next pointers to find the element you want. This takes O(n) in the worst case.

## Types of Linked Lists

There are several types of linked lists:

- **Singly Linked List**: Each node has a single pointer to the next node.
- **Doubly Linked List**: Each node has two pointers, one to the next node and one to the previous node.
- **Linked List with Sentinels**: A linked list that has a dummy node at the beginning and/or the end of the list. This makes the code simpler because you don't have to deal with special cases when adding or removing nodes.

```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
    
one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
one.next = two
two.prev = one
two.next = three
three.prev = two
head = one

def traverse(node):
    print(node.val)
    if not node.next:
        return 0
    
    return traverse(node.next)

traverse(head)
```