"""
Why use linked lists?

pros:
    Linked list can have its elements to be dynamically allocated.
    Linked list nodes can live anywhere in the memory. Array need sequence of memory to be initiated.

cons:
    Linear look up time in O(n). When looking for a value in a linked list, you have to start from the beginning
    and check one element at a time.

"""

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head


    # Time complexity is O(1)
    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n.get_next() is not None:
            n = n.get_next()
        n.set_next(new_node)

    def insert_after_item(self, x, data):
        n = self.head
        while n is not None:
            if n.data == data:
                break
            n = n.get_next()

        if n is None:
            print('item not in the list')
        else:
            new_node = Node(data)
            new_node.set_next(n.get_next())
            n.set_next(new_node)


    # Time complexity is O(n) -> each time method is called,
    # it will always visit every node in the list but only interact with them once, so n* 1 operations
    def size(self):

        current = self.head
        count = 0

        while current:
            count+=1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()

        if current is None:
            raise ValueError("Data not in the list")

        return current

    def delete(self, data):

        current = self.head

        previous = None

        while current:
            if current.get_data() == data:
                # 찾음
                if previous:
                    previous.set_next(current.get_next())
                else:
                    self.head = current.get_next()
                return True
            else :
                previous = current
                current = current.get_next()

        return False


    def print_list(self):
        if self.head is None:
            return 'Linked list is empty'
        else:
            n = self.head
            l = []
            while n is not None:
                l.append(n.get_data())
                n = n.get_next()

            return l

if __name__ == '__main__':

    linked_list = LinkedList()
    linked_list.insert_at_start(3)
    linked_list.insert_at_start(2)
    linked_list.insert_at_start(4)
    linked_list.delete(2)
    linked_list.insert_at_start(5)
    linked_list.insert_at_start(1)
    linked_list.insert_at_start(7)
    linked_list.insert_at_start(9)
    linked_list.delete(22)
    print(linked_list.print_list())
