class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


def print_singly_linked_list(node):
    if node.head is None:
        print('Linked list is empty')
    else:
        n = node.head
        li = []
        while n is not None:
            li.append(n.data)
            n = n.next
        print(li)


# Complete the insertNodeAtHead function below.

#
# For your reference:

def insertNodeAtHead(llist, data):
    # Write your code here
    s = SinglyLinkedListNode(data)
    s.next = llist
    return s


if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtHead(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist)