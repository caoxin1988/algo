
class ArrayQueue(object):
    def __init__(self, size):
        self.data = [None] * size
        self.size = size
        self.head = 0
        self.tail = 0

    def equeue(self, data : int) -> bool:

        if self.tail == self.size:
            if self.head == 0:      # queue is really full
                print('    -> queue is full')
                return False

            for i in range(self.head, self.tail):       # copy data when no space at tail
                self.data[i - self.head] = self.data[i]

            self.tail = self.tail - self.head
            self.head = 0

        self.data[self.tail] = data
        self.tail += 1

        return True

    def dequeue(self) -> int:

        if self.head == self.tail:
            print('    -> queue is empty, dequeue fail')
            return None

        data = self.data[self.head]
        self.head += 1

        return data
        

def main():
    queue = ArrayQueue(3)

    queue.equeue(1)
    queue.equeue(2)
    queue.equeue(3)
    queue.equeue(4)

    print('data : %s' % queue.dequeue())
    print('data : %s' % queue.dequeue())
    print('data : %s' % queue.dequeue())
    print('data : %s' % queue.dequeue())

if __name__ == '__main__':
    main()