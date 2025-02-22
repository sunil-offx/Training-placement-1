def reverse_linked_list(head):
    prev, curr = None, head
    while curr:
        temp = curr.next
        curr.next = prev
        prev, curr = curr, temp
    return prev
