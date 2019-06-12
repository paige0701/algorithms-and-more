class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.head = -1
        self.tail = -1
        self.maxSize = k
        self.queue = [None] * k

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False

        if self.isEmpty():
            self.head = 0

        self.tail = (self.tail + 1) % self.maxSize

        self.queue[self.tail] = value

        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """

        if self.isEmpty():
            return False

        if self.head == self.tail:
            self.head = -1
            self.tail = -1
            return True

        self.head = (self.head + 1) % self.maxSize

        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1

        return self.queue[self.head]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.head == -1

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return (self.tail + 1) % self.maxSize == self.head


if __name__ == '__main__':
# Your MyCircularQueue object will be instantiated and called as such:
    obj = MyCircularQueue(3)
    print(obj.enQueue(1))
    print(obj.enQueue(2))
    print(obj.enQueue(3))
    print(obj.enQueue(4))
    print(obj.Rear())
    print(obj.isFull())
    print(obj.deQueue())
    print(obj.enQueue(4))
    print(obj.Rear())
