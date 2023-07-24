"""
Remove the nth node from the end of a linked list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n):
    # Create a dummy node to handle the case where the head needs to be removed
    dummy = ListNode(0)
    dummy.next = head

    first = dummy
    second = dummy

    # Move the second pointer n positions ahead
    for _ in range(n + 1):
        second = second.next

    # Move both pointers together until the end of the linked list
    while second is not None:
        first = first.next
        second = second.next

    # Remove the desired node
    first.next = first.next.next

    # Return the head of the modified linked list
    return dummy.next

