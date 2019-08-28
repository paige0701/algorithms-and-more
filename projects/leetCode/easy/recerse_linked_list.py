def reverse_linked_list(head):
    prev = None
    curr = head

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev


if __name__ == '__main__':
    reverse_linked_list([1,2,3,4,5])