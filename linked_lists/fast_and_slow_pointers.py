class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None


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


# Example 1: Given the head of a linked list with an odd number of nodes head, return the value of the node in the
# middle.
#
# For example, given a linked list that represents 1 -> 2 -> 3 -> 4 -> 5, return 3.

# Solution 1 - Iterate
def middle_node_iterate(head: ListNode):
    dummy = head
    length = 0
    while dummy.next:
        length += 1
        dummy = dummy.next
    for _ in range(length // 2):
        head = head.next

    return head.val


# Fast and slow pointers
def middle_node(head: ListNode) -> ListNode:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


# Example 2: 141. Linked List Cycle
#
# Given the head of a linked list, determine if the linked list has a cycle.
#
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously
# following the next pointer.

def has_linked_list_a_cycle(head: ListNode) -> bool:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


# Example 3: Given the head of a linked list and an integer k, return the kth node from the end.
#
# For example, given the linked list that represents 1 -> 2 -> 3 -> 4 -> 5 and k = 2, return the node with value 4,
# as it is the 2nd node from the end.
def find_node(head: ListNode, k: int) -> ListNode:
    slow = head
    fast = head

    for _ in range(k):
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    return slow


# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the
# linked list sorted as well.
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]

def delete_duplicates(head: ListNode) -> ListNode | None:
    if not head:
        return None
    slow = head
    fast = head.next

    while fast:
        if notal == fast.val:
            slow.next = fast.next
            fast = slow.next
        else:
            slow = slow.next
            fast = fast.next
    return head


def delete_duplicates_optimize(head: ListNode) -> ListNode:
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head


if __name__ == "__main__":
    head = fill_linked_list(1, 6, False)
    print(has_linked_list_a_cycle(head))
    print(middle_node(head).val)
    head = fill_linked_list(1, 6, True)
    print(has_linked_list_a_cycle(head))
    head = fill_linked_list(1, 6, False)
    print(find_node(head, 2).val)

    # Input: head = [1, 1, 2, 3, 3]
    # Output: [1, 2, 3]
    one = ListNode(1)
    one_duplicate = ListNode(1)
    one_reduplicate = ListNode(1)
    two = ListNode(2)
    three = ListNode(3)
    three_duplicate = ListNode(3)
    one.next = one_duplicate
    one_duplicate.next = one_reduplicate
    one_duplicate.next = two
    two.next = three
    three.next = three_duplicate
    head = delete_duplicates(one)
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("null")
