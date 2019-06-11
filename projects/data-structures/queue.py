class Queue:

    def __init__(self, max_size):
        self.queue = list()
        self.head=0
        self.tail=0
        self.maxSize = max_size


    def enqueue(self, data):

        # check if the queue is full
        if self.size() >= self.maxSize:
            return "Queue is full"
        else:
            self.queue.append(data)
            self.tail += 1
            return True


    def dequeue(self):

        #check if queue is empty
        if self.size() <= 0:
            self.reset_queue()
            return 'Queue is empty'
        data = self.queue[self.head]
        self.head +=1
        return data


    def size(self):
        return self.tail-self.head


    def reset_queue(self):
        self.tail = 0
        self.head = 0
        self.queue = list()

if __name__ == '__main__':
    q = Queue(5)
    print(q.enqueue(1))
    print(q.enqueue(2))
    print(q.enqueue(3))
    print(q.enqueue(4))
    print(q.enqueue(5))
    print(q.size())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())

