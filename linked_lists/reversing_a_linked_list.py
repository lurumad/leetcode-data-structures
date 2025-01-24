from collections import Counter


class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None

    def __str__(self):
        return f"val: {self.val}"


def fill_linked_list(start: int, end: int, cycle: bool) -> ListNode:
    head = ListNode(start)
    current = head
    for val in range(start + 1, end):
        temp = ListNode(val)
        current.next = temp
        current = temp
    if cycle:
        current.next = head
    return head


def reversing(head: ListNode) -> ListNode:
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


# Example: 24. Swap Nodes in Pairs
#
# Given the head of a linked list, swap every pair of nodes. For example, given a linked list 1 -> 2 -> 3 -> 4 -> 5
# -> 6, return a linked list 2 -> 1 -> 4 -> 3 -> 6 -> 5.
def swap_pair_of_nodes(head: ListNode):
    # Check edge case: linked list has 0 or 1 nodes, just return
    if not head or not head.next:
        return head

    dummy = head.next  # Step 5
    prev = None  # Initialize for step 3
    while head and head.next:
        if prev:
            prev.next = head.next  # Step 4
        prev = head  # Step 3

        next_node = head.next.next  # Step 2
        head.next.next = head  # Step 1

        head.next = next_node  # Step 6
        head = next_node  # Move to next pair (Step 3)

    return dummy


# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of
# the list from position left to position right, and return the reversed list.
def reverse_between(head: ListNode, left: int, right: int) -> ListNode:
    prev = None
    current = head
    counter = 1
    new_head = None
    new_tail = None
    while current:
        if counter == left:
            new_head = current
        if counter == right:
            new_tail = current
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
        counter += 1
    new_head.next = prev
    head.next = new_tail
    prev.next = None
    return head


def print_linked_list(head: ListNode) -> None:
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("null")


if __name__ == "__main__":
    head = fill_linked_list(0, 4, False)
    head = reversing(head)
    print_linked_list(head)
    head = fill_linked_list(0, 6, False)
    head = swap_pair_of_nodes(head)
    print_linked_list(head)
    head = fill_linked_list(1, 6, False)
    head = reverse_between(head, 2, 4)
    print_linked_list(head)

